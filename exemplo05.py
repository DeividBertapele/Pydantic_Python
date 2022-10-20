# Pré validadação -> (pre=True)
# validação por item -> (each_item=True)


from pydantic import BaseModel, validators


class Pedidos(BaseModel):
    ids = list[int]
    

    # @validator('ids', pre=True)
    # def convert_ids(cls, v):
    #     if isinstance(v, str):
    #         return v.split(';')
    #     return v

    @validator('ids', each_item=True) # each_item -> validação por item
    def convert_ids(cls, v):
        if v < 0:
            raise ValueError()
        return v


