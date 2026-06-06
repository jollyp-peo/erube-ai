from app.schemas.prompt_package import (
    PromptPackage,
)


class PromptPackageBuilder:

    def build(
        self,
        shot_plan,
        prompt,
    ):

        style_tags = []

        camera_tags = []

        lighting_tags = [
            "cinematic lighting",
        ]

        if shot_plan.camera_type:

            camera_tags.append(
                shot_plan.camera_type
            )

        if shot_plan.camera_movement:

            camera_tags.append(
                shot_plan.camera_movement
            )

        style_tags.extend(
            [
                "fantasy",
                "cinematic",
                "high detail",
            ]
        )

        return PromptPackage(
            prompt=prompt,
            negative_prompt=(
                "low quality, blurry, "
                "distorted anatomy"
            ),
            style_tags=style_tags,
            camera_tags=camera_tags,
            lighting_tags=lighting_tags,
        )