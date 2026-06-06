from app.schemas.scene_goal import SceneGoal


class SceneDirector:

    def build_goal(
        self,
        scene,
    ):

        summary = (
            scene.get(
                "summary",
                "",
            )
            .lower()
        )

        if "search" in summary:

            return SceneGoal(
                objective=(
                    "Search for information"
                ),
                emotional_tone=(
                    "curious"
                ),
                visual_style=(
                    "fantasy adventure"
                ),
            )

        if "meet" in summary:

            return SceneGoal(
                objective=(
                    "Character interaction"
                ),
                emotional_tone=(
                    "suspenseful"
                ),
                visual_style=(
                    "cinematic dialogue"
                ),
            )

        return SceneGoal(
            objective=(
                "Advance story"
            ),
            emotional_tone=(
                "neutral"
            ),
            visual_style=(
                "cinematic"
            ),
        )