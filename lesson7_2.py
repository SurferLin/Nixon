import tools                                       
    
def main():
    while(True):
        tools.playgame()
        playagain = input("您還要繼續嗎(y,n)?")
        if playagain == 'n':
            break

    print("遊戲結束")
    
if __name__ == "__main__":
    main()