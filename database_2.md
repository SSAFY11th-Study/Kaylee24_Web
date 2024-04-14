# N:1

- Many to one relationships  
    : 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계   
- ForeignKey(to, on_delete)  
- on_delete의 'CASCADE'  
    - 부모 객체 삭제 시 이를 참조하는 객체도 삭제  

1. shell_plus 실행 및 게시글 작성  
2. 댓글 생성  
3. shell_plus 실행 및 게시글 작성
4. comment 인스턴스를 통한 article 값 참조하기
5. comment 인스턴스를 통한 article 값 참조하기
6. 두번째 댓글 생성
7. 작성된 댓글 데이터 확인

### 관계 모델 참조
- 역참조 : N:1 관계에서 1에서 N을 참조 또는 조회    
- `a.b_set.all()` : 모델 인스턴스 + related manager(역참조 이름) + QuerySet API  
- Related manager의 이름 : "모델명_set"

### 댓글 구현
[CREATE]  
- CREATE 구현  
    1. CommentForm 정의  
    2. detail view 함수에서 CommentForm을 사용하여 detail 페이지에 렌더링  
    3. CommentForm의 출력 필드 조정하여 외래 키 필드가 출력되지 않도록 함  
    4. url 작성 및 action 작성  
    5. `comments_create` view 함수 정의  
    * save(commit=False)  
        : DB에 저장하지 않고 인스턴스만 반환  
    6. save의 commit 인자를 활용해 외래 키 데이터 추가 입력  

[READ]
- READ 구현  
    - detail view 함수에서 전체 댓글 데이터를 조회  

[DELETE]
- DELETE 구현  
    - 삭제 url 작성  
    - 삭제 view 함수 정의
    - 삭제 버튼 작성