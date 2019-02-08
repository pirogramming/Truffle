# 데이터베이스 설정

* User : id(pk), email, name, password, register_date
* Follow : from_id(fk), to_id(fk), date
* Scrap : user_id(fk), playlist_id(fk), date
* Playlist : id(pk), title, description, content, date, tags, cost
  * Place : id(pk), address, name
    * Place_Content : id(pk), place_id(fk), content
      * Place_Content_Image : id(pk), place_content_id(fk), image
  * Photo : id(pk), photo, 
* Comment : id(pk), user_id(fk), travel_id(fk), content


# Assets
* [서버](https://truffle.run.goorm.io/)
* [아이콘](https://icons8.com/icons/set/truffle)
* [Argon Document](https://demos.creative-tim.com/argon-design-system/docs/getting-started/quick-start.html)
* [Argon GitHub](https://github.com/creativetimofficial/argon-design-system/tree/master/assets)

https://docs.djangoproject.com/en/2.1/topics/forms/

# App
* 프로필, 로그인, 로그아웃, 피드(팔로우), 스크랩
* 여행 일정 게시판
* 코어

# 프론트
* 로그인 전 메인 : 랜딩 페이지
* 로그인 후 메인 : 피드 페이지
* 여행 일정 게시판 : 모든 일정 목록

# 페이지 종류
* 일정 피드 + 추천 게시물 
* 랜딩 페이지
* 일정 등록
* 프로필
-
* 회원가입
* 로그인
* 비밀번호 찾기
* 개인정보 수정


# ㅇㅇㅇ
* 바보
* 건태