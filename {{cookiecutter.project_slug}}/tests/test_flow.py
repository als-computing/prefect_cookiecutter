from ..flow import flow

def test_flow():
    state = flow.run()
    assert state.is_successful()