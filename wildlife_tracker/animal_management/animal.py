from typing import Any, Optional

class Animal:
    def __init__(self,
                animal_id: int,
                species: str,
                age: Optional[int] = None,
                health_status: Optional[str] = None,) -> None:
        self.age = age
        self.animal_id = animal_id
        self.health_status = health_status
        self.species = species


    pass

    def get_animal_details(self) -> dict[str, Any]:
        pass

    def update_animal_details(self, **kwargs: Any) -> None:
        pass
