# 닮은꼴 강아지 테스트 :dog:

[닮은꼴 강아지 테스트 해보기](https://dogsbreedrecognition.netlify.app/)

## **1. 프로젝트 소개**

> **인공지능으로 나와 닮은 견종을 알아보자! '닮은꼴 강아지 테스트 서비스'**

👉 사진을 넣으면 인공지능이 분석해 닮은꼴 강아지를 알려주며 가장 닮은 강아지와 상위 4가지 닮은 종을 알려준다.

**🚀 기술 스택**
|구분|설명|
|:---:|:---:|
|Front|HTML, javascript, CSS|
|MachineLearning|TeachableMachine|
|Crawling|Python(google-image-download)|

## **2. 프로젝트 목표**

- 크롤링을 통해 얻은 이미지로 모델 학습 후, 그 결과를 이용하여 나와 닮은꼴 강아지를 예측한다.

## **3. 기능**

`이미지 크롤링`

- google-image-download 모듈 이용해 구글에서 연예인 이미지 크롤링

`모델 학습`

- teachable-machine에 연예인 별 17개의 클래스 생성 후 이미지 추가하여 모델 학습

`메인 화면`

- 확인할 이미지 업로드를 위한 'file-upload-input' 구현
- 이미지를 target으로 하여 예측 시작시 로딩 이미지 등장

`결과 화면`

- 가장 확률이 높은 결과를 가장 상위에 보이도록 구현
- jquery의 'easy-pie-chart' 이용해 상위 4가지 닮은꼴 강아지 출력
- '다른 사진으로 재시도' 클릭시 modal 창 등장하며 한 번 더 클릭시 메인 화면으로 이동

`반응형 UI`

- 유저가 주로 모바일로 이용한다는 점을 고려하여 반응형 UI 구현
