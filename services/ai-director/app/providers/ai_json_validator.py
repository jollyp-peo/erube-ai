class AIJSONValidator:

    @staticmethod
    def validate_scene_goal(
        data,
    ):

        required = [
            "objective",
            "emotional_tone",
            "visual_style",
        ]

        for field in required:

            if field not in data:

                raise ValueError(
                    f"Missing field: {field}"
                )

        return True

    @staticmethod
    def validate_shot_goal(
        data,
    ):

        required = [
            "purpose",
            "framing_intent",
            "narrative_intent",
        ]

        for field in required:

            if field not in data:

                raise ValueError(
                    f"Missing field: {field}"
                )

        return True