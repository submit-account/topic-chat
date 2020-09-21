# topic-chat

<p float="left" align="center">
    <img width="900" src="http://nlp.dothome.co.kr/model1.png" />  
</p>
Dual WGAN 기반 페르소나 챗봇 모델을 일부 변형하여 국립국어연구원에서 공개한 구어 말뭉치와 한국정보화진흥원에서 공개한 주제 기반 말뭉치(한국어 대화 데이터)를 이용하여 학습한 챗봇입니다.

## Demo

http://nlp.dothome.co.kr/topic_chat.html

좌측 상단의 입력 텍스트 박스에 입력할 발화를 기재한 후 엔터 키를 누르면 모델의 답변이 화면에 출력됩니다.

답변은 1차 보고서 3.1절에서 설명한 복합 표현 단위로 출력됩니다.

생성되는 토큰 종류는 다음과 같습니다.

- `<SP>`: 띄어쓰기
- #이 부착된 토큰: 음절 단위로 생성된 토큰
- 그 외의 토큰: 형태소 단위로 생성된 토큰
  
데모에서 사용할 수 있는 옵션 종류는 다음과 같습니다.
| option | description |
| :-----: | :-------------------------------------- |
| 1 | 두 번째 줄의 radio button을 이용해 대화 주제를 정할 수 있습니다. chit-chat을 제외한 부분은 챗봇이 해당 주제의 점원 역할을 하고 사용자는 고객 입장에서 발화하는 것을 기준으로 합니다. |
| 2 | 세 번째 줄의 직전 context 반영 버튼은 모델의 입력을 single-turn으로 할지 multi-turn으로 할지 정해주는 옵션다. 버튼 클릭 시 이전 발화도 최대 두 개까지 입력으로 함께 들어갑니다. |

현재 데모가 통신하는 모델은 1차 보고서에 기재된 전체 데이터(약 46,000 개)를 이용해 학습한 모델입니다.

실험을 위한 데모 학습용 데이터를 4-turn으로 사용했으므로 모델은 현재 사용자 입력과 이전 발화 한 쌍만 입력으로 받습니다. 따라서 직전 대화 한 쌍 외의 정보는 모델의 입력으로 사용되지 않습니다. 현재 데모에서는 긴 담화에 대한 문맥 반영은 기대할 수 없으며, 추후 10개의 turn까지 반영할 수 있도록 학습할 예정입니다.

그리고 '안녕', '안녕하세요'와 같은 인사말의 경우 학습 데이터에 없어 적절한 응답이 나오지 않을 수 있으니 테스트 시 참고 부탁드립니다.
## Training Details

| param | size |
| ----------------------: | -------------: |
| max_encoder_length      |             50 |
| max_encoder_char_length |             10 |
| max_decoder_length      |             50 |
| morph_embedding_size    |            300 |
| syllable_embedding_size |             50 |
| mixed_embedding_size    |            300 |
| topic_embedding_size    |            100 |
| filter_sizes            |        '1,2,3' |
| num_filters             |            100 |
| context_size            |              2 |
| hidden_size             |            300 |
| topic_size              |              9 |
| z_size                  |            200 |
| discriminator_z_size    |            400 |
| beam_width              |              5 |
| n_critic                |              5 |
| batch_size              |             64 |
| keep_prob               |            0.8 |
| decoder_learning_rate   | 0.001 ~ 0.0001 |
| z_learning_rate         |        0.00002 |
| response_learning_rate  |        0.00005 |

## Updates
20/09/15: 데모 페이지 링크 업로드

20/09/15: `preprocessing` 공개 데이터(국립국어연구원 구어 데이터, aihub 한국어 대화 데이터) 정제 코드 업로드

20/09/15: 데모와 모델(v1.0.0) 연결 - 1차 심사용 유투브 영상 제출 시 사용한 모델

20/09/17: Readme 파일에 이전 컨텍스트 반영 정도에 대한 설명 추가

20/09/18: Readme 파일에 설명 추가, 연결 모델 변경(v1.1.0)

20/09/21: 연결 모델 변경(v1.2.0)
