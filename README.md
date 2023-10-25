# test-server
여러가지 기능 테스트 용 서버


### 실행
--reload : 코드 변경후 서버 재시작


``` 
uvicorn main:app --reload
```

### api 문서 보기
 대화형 : http://127.0.0.1:8000/docs <br>
 대안형 : http://127.0.0.1:8000/redoc

### mysql 도커 연결
-p: 포트 맵핑
-p 3306:3306 : 호스트의 3306 와 컨테이너 안의 3306번 포트 연결
-e : 환경변수 지정
-d : detach 옵션 (백그라운드에서 동작하게 하는 옵션)
-v : 볼륨옵션 (컨테이너를 종료하게되면 데이터 모두 삭제됨) 
    아래의 코드는 로컬 데이터베이스(todos)라는 곳에 저장

- docker ps : 이미지 확인
- dokcer logs todos: todos라는 컨테이너의 로그 확인
- docker volume ls: 도커 이미지의 볼륨
- docker exec -it todos bash: todos의 배쉬 사용
```
# 로컬에 3306포트를 사용하고 있어 3307포트로 연결
docker run -p 3307:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=todos -d -v todos:/db --name todos mysql:8.0

docker ps

docker logs todos

docker volume ls

docker exec -it todos bash
```