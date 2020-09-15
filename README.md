# topic-chat

## Demo

http://nlp.dothome.ac.kr/topic_chat.html

좌측 상단의 입력 텍스트 박스에 입력할 발화를 기재한 후 엔터 키를 누르면 모델의 답변이 화면에 출력된다. 답변은 1차 보고서 3.1절에서 설명한 복합 표현 단위로 출력된다. 생성되는 토큰 종류는 다음과 같다.

- `<SP>`: 띄어쓰기
- #이 부착된 토큰: 음절 단위로 생성된 토큰
- 그 외의 토큰: 형태소 단위로 생성된 토큰
  
데모에서 사용할 수 있는 옵션 종류는 다음과 같다.
| option | description |
| :-----: | :-------------------------------------- |
| 1 | 두 번째 줄의 radio button을 이용해 대화 주제를 정할 수 있다. chit-chat을 제외한 부분은 챗봇이 해당 주제의 점원 역할을 하고 사용자는 고객 입장에서 발화하면 된다. |
| 2 | 세 번째 줄의 직전 context 반영 버튼은 모델의 입력을 single-turn으로 할지 multi-turn으로 할지 정해주는 옵션이다. 버튼 클릭 시 이전 발화도 최대 두 개까지 입력으로 함께 들어간다. |

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

## Source
20/09/15: `preprocessing` 공개 데이터(국립국어연구원 구어 데이터, aihub 한국어 대화 데이터) 정제 코드 업로드
