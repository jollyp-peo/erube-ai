from app.schemas.shot_goal import ShotGoal


class ShotDirector:

    def build_goal(
        self,
        shot,
    ):

        title = (
            shot.get(
                "title",
                "",
            )
            .lower()
        )

        if "establishing" in title:

            return ShotGoal(
                purpose=(
                    "Introduce environment"
                ),
                framing_intent=(
                    "Show scale and setting"
                ),
                narrative_intent=(
                    "Orient audience"
                ),
            )

        if "introduction" in title:

            return ShotGoal(
                purpose=(
                    "Introduce character"
                ),
                framing_intent=(
                    "Focus attention"
                ),
                narrative_intent=(
                    "Present important character"
                ),
            )

        return ShotGoal(
            purpose=(
                "Advance story"
            ),
            framing_intent=(
                "Support scene"
            ),
            narrative_intent=(
                "Move narrative forward"
            ),
        )