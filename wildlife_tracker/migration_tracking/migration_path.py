from typing import Optional

class MigrationPath:
    def __init__(self,
                 path_id: int,
                 start_location: Habitat,
                 destination: Habitat,
                 species: str,
                 duration: Optional[int] = None) -> None :
        self.path_id = path_id
        self.start_location = start_location
        self.destination = destination
        self.species = species
        self.duration = duration
    
    def update_migration_path_details(self, **kwargs) -> None:
        pass

    def get_migration_path_details(self) -> dict:
        pass
