def get_middle(s):
    """Get the Middle Character

    Args:
        s (str): description'

    Returns:
        get_middle(s): Coupole of strings (pair) and doubled middle char (odd)         
    """    
    return s[(len(s)-1)//2:(len(s)+2)//2]