from app.schemas.memory_state import MemoryState


class ContinuityValidator:

    def validate(
        self,
        memory_state: MemoryState,
    ):

        warnings = []

        warnings.extend(
            self.validate_voice_consistency(
                memory_state
            )
        )

        warnings.extend(
            self.validate_wardrobe_consistency(
                memory_state
            )
        )

        return {
            "warnings": warnings,
            "errors": [],
        }

    def validate_voice_consistency(
        self,
        memory_state: MemoryState,
    ):

        warnings = []

        seen = {}

        for character in memory_state.characters:

            if not character.voice_id:

                warnings.append(
                    f"{character.name} has no assigned voice."
                )

                continue

            existing = seen.get(
                character.character_id
            )

            if (
                existing
                and existing != character.voice_id
            ):

                warnings.append(
                    f"{character.name} has multiple voices assigned."
                )

            seen[
                character.character_id
            ] = character.voice_id

        return warnings

    def validate_wardrobe_consistency(
        self,
        memory_state: MemoryState,
    ):

        warnings = []

        wardrobe_map = {}

        for wardrobe in memory_state.wardrobes:

            existing = wardrobe_map.get(
                wardrobe.character_id
            )

            if (
                existing
                and existing != wardrobe.outfit_name
            ):

                warnings.append(
                    f"Character wardrobe changed from "
                    f"{existing} to "
                    f"{wardrobe.outfit_name}"
                )

            wardrobe_map[
                wardrobe.character_id
            ] = wardrobe.outfit_name

        return warnings