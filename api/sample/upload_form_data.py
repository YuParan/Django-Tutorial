import logging

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from api.response import NamelessServer_Response

from django import forms

from PIL import Image
import pandas as pd

logger = logging.getLogger(__name__)


class UploadFileForm(forms.Form):
    """
    데이터를 어떠한 필드로 받을지 지정합니다.
    해당 필드에 적합한 데이터가 존재하는 경우, class 의 내부 변수 self.is_valid = True 로 호출될 수 있습니다
    각 필드의 데이터 존재 여부에 대해 And 형식으로 동작하므로 이곳에서 언급한 모든 필드의 데이터가 존재 해야
    self.is_valid = True 로 나타납니다
    아무 필드도 지정하지 않는 경우 (설령 입력되는 파일이 없더라도) self.is_valid 의 Default 값인 True 가 출력됩니다
    """
    # title = forms.CharField()
    image = forms.FileField()
    dataframe = forms.FileField()


class UploadFormData(APIView):
    """ Postman 을 활용해서 테스트를 진행할 경우, Request 전송방식을 form-data 로 지정해줘야 합니다
        text 를 받는 경우, key(type=text) , File 이 입력되는 경우 key(type=file) 로 지정해줘야 합니다
        테스트용 Image & CSV 파일 처리를 위해, Pillow, Pandas 라이브러리가 필요합니다 """
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        :action:
            Django 에서 POST(파일) Request 와 그 처리를 위한 예시 API 입니다.
            form-data 형식으로 parameter 와 file 을 입력받아, 업로드 된 file 의 내부 정보를 응답합니다.
        :param: request parameter
            "is_save": (int) 업로드 된 파일의 저장 여부. 0 or 1
                       ! 주의 ! : form-data 형식의 경우, 모든 파라미터는 str 타입으로 파싱합니다.
            "image": (file) Image File
            "dataframe": (file) CSV File
        :return: response payload
            "is_save": (bool) 업로드 된 파일의 저장 여부
            "image": {
                "width": (int) 업로드 된 이미지의 가로 픽셀
                "height": (int) 업로드 된 이미지의 세로 픽셀
            },
            "dataframe": {
                "columns": (list) 업로드 된 dataframe 의 columns
                "length": (int) 업로드 된 csv dataframe 의 전체 데이터 길이
        """
        args = dict()
        args["is_save"] = request.data.get("is_save", "0")  # Save True="1" / False="0"
        args["image"] = request.data.get("image")
        args["dataframe"] = request.data.get("dataframe")

        # 필수 Parameter Check
        required_parameters = ["image", "dataframe"]
        if any(args[rq] is None for rq in required_parameters):
            logger.error(args)
            return NamelessServer_Response(
                400,
                "파라미터가 존재하지 않습니다",
                {}
            )

        # 'is_save' Parameter Type Check
        if args['is_save'] == "0" or args['is_save'] == "1":
            args['is_save'] = bool(int(args['is_save']))
        else:
            return NamelessServer_Response(
                400,
                f"Boolean 처리 할 수 없는 파라미터 입니다. 0 또는 1 값이여야 합니다. input: {args['is_save']}",
                {}
            )

        # Get Uploaded File
        form = UploadFileForm(request.POST, request.FILES)
        args["image"] = request.FILES["image"]
        args["dataframe"] = request.FILES["dataframe"]
        logger.info(f"image-name : {args['image']} & dataframe-name : {args['dataframe']}")

        """
        # File Form 에 대한 사용 가이드
        print(">" * 30)
        print(form)
        print(form.files)
        print("=" * 10)
        print(args["image"])  # 파일 이름 출력
        print(args["image"].file.read())
        # 파일의 BytesIO 정보 출력 - read() 실행 시 커서가 파일의 맨 마지막으로 이동하므로 이에 주의
        print(args["image"].size)  # 파일 용량 (Byte)
        print(args["image"].content_type)  # 파일의 타입
        print("<" * 30)
        """

        if form.is_valid():
            try:
                # Read Files
                image = Image.open(args['image'])  # type : PIL.Image
                dataframe = pd.read_csv(args['dataframe'])  # type : pandas.DataFrame
            except Exception as e:
                logger.error(e)
                return NamelessServer_Response(
                    400,
                    f"PIL.Image 와 pandas.DataFrame 으로 변환 할 수 없는 파일 형식 입니다. \n "
                    f"image's Type: {args['image'].content_type} \n "
                    f"dataframe's Type: {args['dataframe'].content_type}",
                    {}
                )
        else:
            return NamelessServer_Response(
                400,
                "처리 할 수 없는 형식의 파일이 포함되어 있습니다.",
                {}
            )

        if args['is_save']:
            image.save("save.png")
            dataframe.to_csv("save.csv")

            # # chunk 로 조각내어 저장하기
            # with open('save-chunk.png', 'wb+') as destination:
            #     for chunk in request.FILES['image'].chunks():
            #         destination.write(chunk)

            logger.info("Save Files")

        # 최종 정상 응답
        return NamelessServer_Response(
            200,
            "파일과 파라미터를 정상적으로 처리하였습니다.",
            {
                "is_save": args['is_save'],
                "image": {
                    "width": image.size[0],
                    "height": image.size[1]
                },
                "dataframe": {
                    "columns": dataframe.columns.tolist(),
                    "length": len(dataframe)
                }
            }
        )
