# Uigkwag-Lee

## 멜론차트 분석

1. 데이터 수집
 - 2021년 멜론 차트 분석을 통한 노래 추천시스템 및 단어들의 가중치를 조사하여 6월 달에 어떤 단어가 주를 이룬 노래가 구성될지 시계열 분석을 해보려 한다. 이를 위해 데이터를 수집해줘야 하는데 따로 존재하지 않기에 셀레니움을 통한 웹크롤링을 이용하여 csv 파일로 저장하여 만든다. 데이터 수집 중 코랩을 사용하려고 했지만,  driver를 화면을 오픈해주는 과정에서 오류가 나기 때문에 vscode를 이용하여 작성하였다.




2. 전처리 및 EDA
 - 따로 Csv를 불러오는 과정에서 데이터 전처리를 안 해줬기에 전처리 및 EDA를 해줘야 된다. EDA과정 중 노래의 명사만 뽑아 WorCloud하거나 가수 별 연간 차트 통계 및 사람들의 연간 선호 장르 통계를 보여주려고 한다. 추천 시스템의 경우 노래 간의 상관 계수를 사용하여 상관계수가 높은 것을 추천해주는 협업 필터링과 가사를 조사하여 비슷한 유형의 노래를 추천해주는 내용기반 필터링을 사용해볼 예정이다. 시계열 분석의 경우 단어를 그냥 사용할 수가 없기에 TF-IDF를 사용하여 가중치를 Numerical하게 바꿔 1월 ~ 5월까지의 단어 별 가중치를 구해줘서 사용해볼 예정이다.


- 2021-07-10
 1. 협업 필터링을 사용하기 위해 멜론 웹 크롤링을 통해 노래 별 별점(1점~5점)을 추가해주려 했지만 없었기에 노래 별 앨범의 점수를 csv파일에 feature로 추가해줬음
 2. csv 파일 생성 과정 추가적인 전처리를 미리 해줬음
 3. 각종 불필요한 단어들을 삭제하는 전처리 과정을 신경을 써 명사만 출력되게끔 하여 wordcloud의 EDA과정을 신경을 씀

- 2021-07-18
 1. 가사별 단어의 코사인 유사도를 분석하여 콘텐츠 기반 필터링을 이용해 추천시스템을 구현

- 2021-07-26
 1. PPT 제작(진행)
