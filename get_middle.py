def get_middle(s):
    """Get the Middle Character

    Args:
        s (str): any string

    Returns:
        get_middle(s): Couple of strings (pair) and doubled middle char (odd)         
    """    
    return s[(len(s)-1)//2:(len(s)+2)//2]