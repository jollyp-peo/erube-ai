from app.schemas.storyboard_plan import (
    StoryboardPlan,
)


class StoryboardDirector:

    def build(
        self,
        shot_plan,
        storyboard_prompt,
    ):

        return StoryboardPlan(
            shot_id=shot_plan.shot_id,
            storyboard_prompt=storyboard_prompt,
            negative_prompt=(
                shot_plan
                .prompt_package
                .negative_prompt
            ),
        )