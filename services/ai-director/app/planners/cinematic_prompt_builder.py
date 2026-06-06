class CinematicPromptBuilder:

    def build(
        self,
        shot_plan,
    ):

        parts = []

        # Shot title

        parts.append(
            shot_plan.title
        )

        # Location

        if shot_plan.location:

            location_text = (
                f"{shot_plan.location.name}"
            )

            if (
                shot_plan.location.time_of_day
            ):

                location_text += (
                    f", "
                    f"{shot_plan.location.time_of_day}"
                )

            parts.append(
                location_text
            )

        # Characters

        for character in (
            shot_plan.characters
        ):

            if character.wardrobe:

                parts.append(
                    f"{character.name} "
                    f"wearing "
                    f"{character.wardrobe}"
                )

            else:

                parts.append(
                    character.name
                )

        # Directing intent

        if shot_plan.goal:

            parts.append(
                shot_plan.goal.framing_intent
            )

        # Camera

        if shot_plan.camera_type:

            parts.append(
                f"{shot_plan.camera_type} shot"
            )

        if shot_plan.camera_movement:

            parts.append(
                shot_plan.camera_movement
            )

        # Cinematic quality tags

        parts.extend(
            [
                "cinematic lighting",
                "high detail",
                "epic fantasy film",
            ]
        )

        return ", ".join(
            parts
        )