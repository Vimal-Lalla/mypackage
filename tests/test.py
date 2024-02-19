from mypackage import mymodule

def test_top_n():
    """
    Make sure top_n works correctly
    """
    assert mymodule.top_n([8,3,2,7,4],3) == [8,7,4] , "Should be [8,7,4]"
    assert mymodule.top_n([8,3,2,7,4],2) == [8,7] , "Should be [8,7]"
    assert mymodule.top_n([8,3,2,7,4],1) == [8]   , "Should be [8]"