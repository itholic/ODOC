# Pull Request

Pull Request(이하 PR)란, 본인이 변경한 내용을 리모트 저장소에 바로 반영하지 않고 커밋 권한이 있는 다른 사용자들에게 검토 후 commit여부를 결정하는 개념이다.

## 과정

1. 작업을 원하는 리모트 저장소 Fork

2. Fork한 저장소를 다운로드(원본 저장소가 아님)
> git clone https://github.com/itholic/spark.git

3. 원본 저장소를 remote 저장소에 추가
> git remote add upstream https://github.com/apache/spark.git
> 'upstream'은 별명이지만, 일반적으로 upstream이라고 쓴다.

4. 원격 저장소 추가 확인
> git remote -v

5. 작업 브랜치 생성
> git checkout -b dev

6. 수정사항 add
> git add -A

7. 수정사항 commit
> git commit

8. 수정사항 push
> git push origin dev

9. Fork한 저장소로 가보면 Pull Request가 생성되어있는 것을 확인할 수 있음 (Compare & pull request)

10. 설명을 적고, Create Pull request를 누르면 완료