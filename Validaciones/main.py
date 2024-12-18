from typing import Optional
from pydantic import BaseModel, ValidationError, field_validator, model_validator

class User(BaseModel):
    username: str
    password: str
    repeat_password: str
    email: str
    age: Optional[int] = None  # Campo opcional con valor por defecto None

    # Validador de campo para username
    @field_validator('username')
    def username_validation_length(cls, username: str) -> str:
        if len(username) < 4:  # Longitud mínima: 4 caracteres
            raise ValueError('La longitud mínima es de 4 caracteres.')
        if len(username) > 50:  # Longitud máxima: 50 caracteres
            raise ValueError('La longitud máxima es de 50 caracteres.')
        return username

    # Validador de modelo para validar que las contraseñas coinciden
    @model_validator(mode="before")
    def check_passwords_match(cls, values):
        password = values.get('password')
        repeat_password = values.get('repeat_password')

        if password != repeat_password:
            raise ValueError('Las contraseñas son diferentes.')
        return values

try:
    user1 = User(
        username='am',
        password='password123',
        repeat_password='password123',
        email='info@odigofacilito.com',
        age=10
    )
    print(user1)
except ValidationError as e:
    print(e.json())  # Imprime el error en formato JSON
