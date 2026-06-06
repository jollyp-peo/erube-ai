from app.schemas.shot_plan import (
    CharacterContext,
    LocationContext,
    VoiceContext,
)


class ContextBuilder:

    def build_character_contexts(
        self,
        scene,
        memory_state,
    ):

        contexts = []

        for character in scene.get(
            "characters",
            [],
        ):
            wardrobe_name = None

            for wardrobe in memory_state.wardrobes:
            
                if (
                    wardrobe.character_id
                    == character["character_id"]
                ):
            
                    wardrobe_name = (
                        wardrobe.outfit_name
                    )
            
                    break
            
        
            
            contexts.append(
                CharacterContext(
                    character_id=character[
                        "character_id"
                    ],
                    name=character[
                        "name"
                    ],
                    wardrobe=wardrobe_name,
                )
            )

        return contexts

    def build_location_context(
        self,
        scene,
    ):

        return LocationContext(
            name=scene["location"],
            time_of_day=scene[
                "time_of_day"
            ],
        )
        
        
    def build_voice_context(
        self,
        scene,
        memory_state,
    ):
        for scene_character in scene.get(
            "characters",
            [],
        ):
    
            character_id = (
                scene_character[
                    "character_id"
                ]
            )
    
            for character in (
                memory_state.characters
            ):
    
                if (
                    character.character_id
                    == character_id
                ):
    
                    if not (
                        character.voice_id
                    ):
                        continue
    
                    for voice in (
                        memory_state.voices
                    ):
    
                        if (
                            voice.voice_id
                            == character.voice_id
                        ):
    
                            return VoiceContext(
                                voice_id=voice.voice_id,
                                name=voice.name,
                            )
    
        return None