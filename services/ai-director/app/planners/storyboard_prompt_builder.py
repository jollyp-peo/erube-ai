class StoryboardPromptBuilder:

    def build(
        self,
        shot_plan,
    ):

        return (
            shot_plan.prompt_package.prompt
        )