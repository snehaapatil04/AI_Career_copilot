import os
import time
from google import genai


# ============================================================
# GEMINI CONFIGURATION
# ============================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. "
        "Set it in PowerShell before starting Flask."
    )

client = genai.Client(api_key=api_key)


# ============================================================
# RESUME ANALYZER
# ============================================================

def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are an expert technical recruiter, career advisor,
ATS resume reviewer, and hiring manager.

Analyze the candidate's resume specifically for the
target career role.

==================================================
TARGET ROLE
==================================================

{user_goal}

==================================================
RESUME
==================================================

{resume_text}

==================================================
STRICT ANALYSIS RULES
==================================================

1. Analyze the ENTIRE resume before making conclusions.

2. Check all relevant sections, including:

   - Professional Summary
   - Technical Skills
   - Projects
   - Certifications
   - Experience
   - Education

3. NEVER claim a skill is missing if it appears anywhere
   in the resume.

4. Classify skills into:

   A. Clearly demonstrated
   B. Partially demonstrated
   C. Genuinely missing

5. Do NOT invent:

   - Skills
   - Projects
   - Experience
   - Certifications
   - Achievements
   - Technologies
   - Job responsibilities

6. Evaluate the candidate ONLY against the target role.

7. Do not penalize the candidate for technologies that
   are irrelevant to the target role.

8. The candidate is an entry-level/fresher candidate.
   Keep recommendations realistic.

9. The learning roadmap must focus ONLY on:
   - genuinely missing skills
   - clearly weak skills

10. If the resume already demonstrates a skill,
    DO NOT recommend learning that skill as a missing skill.

11. Recommendations must be specific and practical.

12. Use evidence from the actual resume whenever possible.

==================================================
REQUIRED OUTPUT
==================================================

MATCH SCORE:
Give a score from 0 to 100.

Briefly explain why the candidate received this score.

==================================================

RELEVANT SKILLS FOUND:

List the skills from the resume that are relevant
to the target role.

==================================================

STRENGTHS:

Explain the strongest relevant:

- Technical skills
- Projects
- Certifications
- Experience
- Achievements

==================================================

SKILLS PARTIALLY DEMONSTRATED:

List skills that appear in the resume but have:

- Limited evidence
- Weak project usage
- Basic exposure
- Need stronger demonstration

If there are none, write:

None identified.

==================================================

GENUINELY MISSING SKILLS:

List ONLY important skills that are relevant to the
target role but are not found in the resume.

If there are no major gaps, write:

No major skill gaps identified.

==================================================

RESUME RECOMMENDATIONS:

Give 4-6 specific recommendations.

For every recommendation explain:

WHAT:
What should change?

WHY:
Why does it matter for the target role?

Do not tell the candidate to add skills they do not have.

==================================================

PERSONALIZED ROADMAP:

Create a practical roadmap based ONLY on missing
or weak skills.

Use this structure:

Week 1:
Topic:
What to learn:
Practice:

Week 2:
Topic:
What to learn:
Practice:

Continue only when necessary.

Do not create unnecessary learning weeks.

==================================================

PROJECT SUGGESTIONS:

Suggest 2-3 projects that would strengthen the
candidate's profile for the target role.

For every project include:

Project Name:
Technologies:
What to Build:
Why It Helps:

Do not simply duplicate projects already present
in the resume.

==================================================

FINAL ASSESSMENT:

Give a concise assessment covering:

1. Current suitability
2. Biggest strength
3. Biggest gap
4. Most important next step

==================================================

FINAL IMPORTANT RULE:

Everything about the candidate must be based on the
resume provided above.

Do not hallucinate.

Do not assume skills that are not present.

Do not claim a skill is missing when it appears
anywhere in the resume.

Make the analysis specific to the target role.
"""


    # ========================================================
    # GEMINI REQUEST WITH RETRY
    # ========================================================

    max_attempts = 3

    for attempt in range(max_attempts):

        try:

            print(
                f"Gemini request attempt "
                f"{attempt + 1}/{max_attempts}..."
            )

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            # ------------------------------------------------
            # Check response
            # ------------------------------------------------

            if response and response.text:

                print("Gemini analysis successful.")

                return {
                    "analysis": response.text,
                    "career_goal": user_goal
                }

            # Empty response

            return {
                "analysis": "Gemini returned an empty response.",
                "career_goal": user_goal
            }

        except Exception as e:

            error_message = str(e)

            print(
                f"Gemini error on attempt "
                f"{attempt + 1}: {error_message}"
            )

            # ------------------------------------------------
            # Temporary Gemini 503 error
            # ------------------------------------------------

            if (
                "503" in error_message
                or "UNAVAILABLE" in error_message
            ):

                # If attempts remain, wait and retry

                if attempt < max_attempts - 1:

                    wait_time = 3 * (attempt + 1)

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                    continue

                # All retries failed

                return {
                    "analysis": (
                        "Gemini is temporarily unavailable "
                        "because the AI service is experiencing "
                        "high demand. Please try again in a "
                        "few moments."
                    ),
                    "career_goal": user_goal
                }

            # ------------------------------------------------
            # Other Gemini/API error
            # ------------------------------------------------

            return {
                "analysis": f"Gemini API error: {error_message}",
                "career_goal": user_goal
            }


    # ========================================================
    # FALLBACK
    # ========================================================

    return {
        "analysis": (
            "Unable to generate the career analysis. "
            "Please try again."
        ),
        "career_goal": user_goal
    }