def recommend_date(region, budget, activity):
    if region == "1":
        region_name = "평택"
    elif region == "2":
        region_name = "강남"
    elif region == "3":
        region_name = "김포"
    else:
        return "올바른 지역 번호를 입력해주세요."

    if budget == "1":
        budget_name = "1만원 이하"
    elif budget == "2":
        budget_name = "3만원 이하"
    elif budget == "3":
        budget_name = "상관없음"
    else:
        return "올바른 예산 번호를 입력해주세요."

    if activity == "1":
        activity_name = "맛집 데이트"
    elif activity == "2":
        activity_name = "산책 데이트"
    elif activity == "3":
        activity_name = "영화 데이트"
    elif activity == "4":
        activity_name = "카페 데이트"
    else:
        return "올바른 활동 번호를 입력해주세요."

    # 추천 결과 만들기
    if region == "1":  # 평택
        if activity == "1":
            if budget == "1":
                place = "가성비 분식집, 학교 근처 햄버거집"
            elif budget == "2":
                place = "파스타집, 고기집"
            else:
                place = "분위기 좋은 레스토랑"
        elif activity == "2":
            place = "평택호 산책길, 동네 공원, 캠퍼스 산책"
        elif activity == "3":
            place = "영화관, 집에서 넷플릭스 데이트"
        elif activity == "4":
            if budget == "1":
                place = "저가 카페, 테이크아웃 카페"
            elif budget == "2":
                place = "디저트 카페, 감성 카페"
            else:
                place = "분위기 좋은 대형 카페"

    elif region == "2":  # 강남
        if activity == "1":
            if budget == "1":
                place = "가성비 맛집, 분식집"
            elif budget == "2":
                place = "파스타집, 초밥집"
            else:
                place = "고급 레스토랑"
        elif activity == "2":
            place = "가로수길 산책, 한강공원"
        elif activity == "3":
            place = "영화관, 코엑스 데이트"
        elif activity == "4":
            if budget == "1":
                place = "프랜차이즈 카페"
            elif budget == "2":
                place = "감성 카페, 디저트 카페"
            else:
                place = "루프탑 카페, 분위기 좋은 카페"

    elif region == "3":  # 김포
        if activity == "1":
            if budget == "1":
                place = "분식집, 버거집"
            elif budget == "2":
                place = "고기집, 파스타집"
            else:
                place = "분위기 좋은 맛집"
        elif activity == "2":
            place = "아라뱃길 산책, 공원 데이트"
        elif activity == "3":
            place = "영화관, 실내 데이트"
        elif activity == "4":
            if budget == "1":
                place = "저렴한 카페"
            elif budget == "2":
                place = "디저트 카페"
            else:
                place = "뷰 좋은 카페"

    result = (
        f"\n오늘 {region_name}에서 {budget_name} 예산으로 즐길 수 있는 "
        f"{activity_name}를 추천할게요!\n"
        f"추천 장소: {place}\n"
        f"오늘은 {activity_name}가 잘 어울리는 하루예요!"
    )

    return result


print("=== 데이트 추천 프로그램 ===")

print("\n[지역 선택]")
print("1. 평택")
print("2. 강남")
print("3. 김포")
region = input("지역을 선택하세요: ")

print("\n[예산 선택]")
print("1. 1만원 이하")
print("2. 3만원 이하")
print("3. 상관없음")
budget = input("예산을 선택하세요: ")

print("\n[데이트 종류 선택]")
print("1. 맛집 데이트")
print("2. 산책 데이트")
print("3. 영화 데이트")
print("4. 카페 데이트")
activity = input("데이트 종류를 선택하세요: ")

result = recommend_date(region, budget, activity)
print(result)