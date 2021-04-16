import random
import warnings
import secrets
from datetime import datetime, date

# import tensorflow as tf
import numpy as np
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView
from rest_framework.response import Response

from medical_iot.settings import UPLOAD_FOLDER
from .models import SampleData
from .serializer import PredictionSerializer, ResultSerializer
# import tensorflow as tf
#
# tf.keras.backend.clear_session()
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.models import load_model
from skimage.transform import resize
from skimage.morphology import label
import io
from PIL import Image

from patients.models import Patient
from testtype.models import TestType

warnings.filterwarnings('ignore', category=UserWarning, module='skimage')

model = None

IMG_WIDTH = 512
IMG_HEIGHT = 512
IMG_CHANNELS = 1

seed = 42
random.seed = seed
np.random.seed(0)
sizes_test = []


# class ImageModel:
#     def pre_load_model(self):
#         global model
#         model = load_model(
#             r'/home/wappnet01/Harsh/officeworkspace/medical_iot/imageprediction/samplemodel/model-POSITIVE-198-1.h5',
#             compile=False)
#         model._make_predict_function()
#         print(model.summary())
#
#     def rle_encoding(self, x):
#         dots = np.where(x.T.flatten() == 1)[0]
#         run_lengths = []
#         prev = -2
#         for b in dots:
#             if (b > (prev + 1)):
#                 run_lengths.extend((b + 1, 0))
#                 run_lengths[-1] += 1
#                 prev = b
#         return run_lengths
#
#     def prob_to_rles(self, x, cutoff=0.3):
#         lab_img = label(x > cutoff)
#         for i in range(1, lab_img.max() + 1):
#             yield self.rle_encoding(lab_img == i)
#
#     def prepare_image(self, image, target):
#         if image.mode != "RGB":
#             image = image.convert("RGB")
#
#         print(image.size)
#         image = image.resize(target)
#         image = img_to_array(image)
#         return image


# Create your views here.
class ImagePredection(APIView):
    def fileunique(self, filename):
        file, extension = secrets.token_hex(10)[1::3], filename.split('.')[1]
        return "{}-{}.{}".format(file, str(datetime.now()).split(' ')[0][5:10], extension)

    def post(self, request):
        if request.data['mode'] == 'autoscope':
            if Patient.objects.filter(patient_email=request.data['patient_email']).exists():
                if TestType.objects.filter(disease_name=request.data['disease_name']).exists():

                    # imgobj = ImageModel()
                    my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]

                    file = request.FILES['image']
                    user_id = {"user_id": Token.objects.get(key=my_token).user_id}
                    patient_id = {"patient_id": Patient.objects.get(patient_email=request.data['patient_email']).id}
                    test_type = {"test_type": TestType.objects.get(disease_name=request.data['disease_name']).id}
                    unique_filename = self.fileunique(file.name)
                    IMGSTO = '{}{}'.format(UPLOAD_FOLDER, unique_filename)

                    image = file.read()
                    f = open(IMGSTO, 'wb+')
                    f.write(image)
                    f.close()

                    # image = Image.open(io.BytesIO(image))
                    #
                    # image = imgobj.prepare_image(image, target=(512, 512))
                    # X_test = image[:, :, 0]
                    # X_test3 = np.expand_dims(X_test, axis=0)
                    # X_test2 = np.expand_dims(X_test3, axis=3)
                    #
                    # imgobj.pre_load_model()
                    # preds_test = model.predict(X_test2)
                    #
                    # preds_test_t = (preds_test > 0.3).astype(np.uint8)
                    # print(preds_test_t)
                    #
                    # sizes_test.append([image.shape[0], image.shape[1]])
                    # preds_test_upsampled = resize(np.squeeze(preds_test), sizes_test[0], mode='constant',
                    #                               preserve_range=True)
                    #
                    # test_rle = list(imgobj.prob_to_rles(preds_test_upsampled))
                    # print(len(test_rle))

                    """
                    dummy
                    """
                    temp = ["Positive", "Negative", "Grade 1", "Grade 2", "Grade 3"]
                    test_rle = random.randint(0, 1024)
                    result = {'result': random.choice(temp)}
                    """
                    dummy ends
                    """
                    image_name = {'image_name': unique_filename}
                    # result_length = {'result_length': len(test_rle)}
                    result_length = {'result_length': test_rle}
                    request_mode = {'mode': 'autoscope'}
                    request.data.pop('image')
                    request.data._mutable = True
                    request_image_name = image_name
                    request_length = result_length
                    request_user = user_id
                    request_patient_id = patient_id
                    request_test_type = test_type
                    request.data.update(request_image_name)
                    request.data.update(request_mode)
                    request.data.update(request_length)
                    request.data.update(result)
                    request.data.update(request_test_type)
                    request.data.update(request_patient_id)
                    request.data.update(request_user)

                    serializer_class = PredictionSerializer(data=request.data)
                    if serializer_class.is_valid():
                        serializer_class.save()
                        return Response({"status": True, "msg": "Successfully uploaded sample"},
                                        status=status.HTTP_200_OK)
                    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"status": False, "msg": "Disease name Not Exist"})
            else:
                return Response({"status": False, "msg": "Patient Not Exist"})
        elif request.data['mode'] == 'ace_it':
            if Patient.objects.filter(patient_email=request.data['patient_email']).exists():
                if TestType.objects.filter(disease_name=request.data['disease_name']).exists():
                    my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
                    user_id = {"user_id": Token.objects.get(key=my_token).user_id}
                    patient_id = {"patient_id": Patient.objects.get(patient_email=request.data['patient_email']).id}
                    test_type = {"test_type": TestType.objects.get(disease_name=request.data['disease_name']).id}
                    """
                    dummy
                    """
                    temp = ["Positive", "Negative", "Grade 1", "Grade 2", "Grade 3"]
                    test_rle = random.randint(0, 1024)
                    result = {'result': random.choice(temp)}
                    """
                    dummy ends
                    """
                    image_name = {'image_name': 'ACE_IT-Test-no_image'}
                    # result_length = {'result_length': len(test_rle)}
                    result_length = {'result_length': test_rle}

                    request.data._mutable = True
                    request_image_name = image_name
                    request_length = result_length
                    request_user = user_id
                    request_patient_id = patient_id
                    request_test_type = test_type
                    request.data.update(request_image_name)
                    request.data.update(request_length)
                    request.data.update(result)
                    request.data.update(request_test_type)
                    request.data.update(request_patient_id)
                    request.data.update(request_user)

                    serializer_class = PredictionSerializer(data=request.data)
                    if serializer_class.is_valid():
                        serializer_class.save()
                        return Response({"status": True, "msg": "Successfully uploaded sample"},
                                        status=status.HTTP_200_OK)
                    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"status": False, "msg": "Disease name Not Exist"})
            else:
                return Response({"status": False, "msg": "Patient Not Exist"})

    def get(self, request):
        results = SampleData.objects.all()
        serializer_class = ResultSerializer(results, many=True)
        return Response(serializer_class.data)
