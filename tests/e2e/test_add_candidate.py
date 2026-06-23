# def test_add_candidate_then_reject(candidate_fixture):
#     candidate_page, candidate = candidate_fixture
#     candidate_page.go_to_add_candidate()
#     candidate_page.add_candidate(candidate)
#     candidate_page.reject_candidate()

# def test_add_candidat(candidate_fixture):
#     candidate_page, candidate = candidate_fixture
#     candidate_page.go_to_add_candidate()
#     candidate_page.add_candidate(candidate)

# def test_add_candidate_then_shortlist(candidate_fixture):
#     candidate_page, candidate = candidate_fixture
#     candidate_page.go_to_add_candidate()
#     candidate_page.add_candidate(candidate)
#     candidate_page.add_candidate_to_shortlist()

# def test_add_candidate(candidate_fixture):
#     candidate_page, candidate = candidate_fixture

#     candidate_page.go_to_add_candidate()
#     candidate_page.add_candidate(candidate)

# def test_add_candidate_then_shortlist(candidate_fixture):
#     candidate_page, candidate = candidate_fixture

#     candidate_page.go_to_add_candidate()
#     candidate_page.add_candidate(candidate)

#     candidate_page.go_to_candidate_list()
#     candidate_page.add_candidate_to_shortlist()

# def test_add_candidate_then_reject(candidate_fixture):
#     candidate_page, candidate = candidate_fixture

#     candidate_page.go_to_add_candidate()
#     candidate_page.add_candidate(candidate)

#     candidate_page.go_to_candidate_list()
#     candidate_page.reject_candidate()


def test_add_candidate_api(page, add_candidate):
    assert add_candidate["data"]["firstName"] is not None
    assert add_candidate["data"]["lastName"] is not None
    assert add_candidate["data"]["email"] is not None