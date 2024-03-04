from model_bakery import baker
from apps.flax_id import get_flax_id

baker.generators.add("flax_id.django.fields.FlaxId", get_flax_id)
