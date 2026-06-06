class PromptBuilder:

    def build(
        self,
        shot_plan,
    ):

        prompt_parts = []

        # Shot goal

        if shot_plan.goal:

            prompt_parts.append(
                shot_plan.goal.purpose
            )

            prompt_parts.append(
                shot_plan.goal.framing_intent
            )

        # Location

        if shot_plan.location:

            prompt_parts.append(
                shot_plan.location.name
            )

            if (
                shot_plan.location.time_of_day
            ):

                prompt_parts.append(
                    shot_plan.location.time_of_day
                )

        # Characters

        for character in (
            shot_plan.characters
        ):

            prompt_parts.append(
                character.name
            )

            if character.wardrobe:

                prompt_parts.append(
                    character.wardrobe
                )

        return ", ".join(
            prompt_parts
        )