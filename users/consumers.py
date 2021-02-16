from django.contrib.auth.models import User
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer

from users.serializers import UserSerializer


class UserConsumer(AsyncAPIConsumer):

    async def connect(self):
        await self.model_change.subscribe()
        return await super().connect()

    @model_observer(User)
    async def model_change(self, message, action=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        user_model = User.objects.all()
        user_serializer = UserSerializer(data=user_model, many=True)
        user_serializer.is_valid()
        return user_serializer.data
