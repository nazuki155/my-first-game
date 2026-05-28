import tkinter
import random

FNT=("System",40)
WIDTH,HEIGHT=960,720
bar_x=WIDTH/2
bar_y=500
enemy_x=WIDTH/2
enemy_y=120
enemy_life=5
bullet_x=0
bullet_y=bar_y
FNT=("System",40)
bullet_st="待機"
enemy_rl=0
enemy_m=0
key=0
time=500
scene="タイトル"


#自分の動き
def move(key):
    global bullet_st,bullet_x,bar_x,enemy_x,enemy_life,scene,time

    if scene=="タイトル" and key.keysym=="s":
        enemy_life=5
        bar_x=WIDTH/2
        enemy_x=WIDTH/2
        time=500
        scene="ゲーム"

    if scene=="ゲーム":
        if key.keysym=="Left":
            bar_x=bar_x-5
        if bar_x-50<0:
            bar_x=50
        
        if key.keysym=="Right":
            bar_x=bar_x+5
        if bar_x+50>WIDTH:
            bar_x=WIDTH-50
        
        if key.keysym=="z" and bullet_st=="待機":
            bullet_st="発射"
            bullet_x=bar_x

            
    if key.keysym=="t" and scene=="勝ち":
            scene="タイトル"

    if key.keysym=="t" and scene=="負け":
            scene="タイトル"
        

#敵の動きを初期化 
def enemy_move():
    global enemy_m,enemy_rl
    enemy_rl=random.randint(0,2)
    enemy_m=random.randint(10,15)
    

        
def main():

        global bar_x,bar_y,bullet_x,bullet_y,bullet_st
        global enemy_x,enemy_y,enemy_m,enemy_rl,enemy_life,scene,time
    
        cvs.delete("all")
        cvs.create_image(WIDTH/2,HEIGHT/2,image=bg)
        cvs.create_image(bar_x,bar_y,image=player)
        cvs.create_image(enemy_x,enemy_y,image=enemy)
        cvs.create_text(150,50,text="ENEMY LIFE",font=FNT,fill="white")


        #敵のライフを表示する
        for i in range(enemy_life):
            cvs.create_text(i*40+300,50,text="■",font=FNT,fill="white")
            
        #タイムを表示する
        cvs.create_text(700,50,text="TIME"+str(time),font=FNT,fill="white")



        if scene=="タイトル":
            cvs.create_text(WIDTH/2,HEIGHT/2,text="SPACE WAR",font=FNT,fill="yellow")
            cvs.create_text(WIDTH/2,HEIGHT/2+50,text="[S]tart",font=FNT,fill="white") 
        #敵の動き
        if scene=="ゲーム":
        
            if enemy_rl==0:
                enemy_x=enemy_x+5
                enemy_m=enemy_m-1
            if enemy_rl==1:
                enemy_x=enemy_x-5
                enemy_m=enemy_m-1
            if enemy_rl>1:
                enemy_m=enemy_m-1
            if enemy_m<=0:
                enemy_move()
        
        #敵が枠からはみ出ないようにする
            if enemy_x<60:
                enemy_x=60
            if enemy_x>WIDTH-60:
                enemy_x=WIDTH-60

        #弾の発射処理 
            if bullet_st=="発射":
                cvs.create_oval(bullet_x-10,bullet_y-10,bullet_x+10,bullet_y+10,
                        fill="yellow")
                bullet_y=bullet_y-20
        
            if bullet_y<-10:
                bullet_st="待機"
                bullet_y=bar_y
            
            #弾の衝突判定
            dx=abs(enemy_x-bullet_x)
            if bullet_st=="発射" and dx<80 and enemy_y>bullet_y:
                bullet_st="待機"
                bullet_x=bar_x
                bullet_y=bar_y
                enemy_life=enemy_life-1

            time=time-1
            if time<0:
                time=0
            #勝つ時    
            if enemy_life<=0:
                scene="勝ち"
            
            #負ける時    
            if time==0:
                scene="負け"
            
        if scene=="勝ち":
                cvs.create_text(WIDTH/2,HEIGHT/2,text="YOU WIN",font=FNT,fill="yellow")
                cvs.create_text(WIDTH/2,HEIGHT/2+50,text="[T]itle",font=FNT,fill="white")

        if scene=="負け":
                cvs.create_text(WIDTH/2,HEIGHT/2,text="YOU LOSE",font=FNT,fill="red")
                cvs.create_text(WIDTH/2,HEIGHT/2+50,text="[T]itle",font=FNT,fill="white") 
            
        root.after(28,main)


root=tkinter.Tk()
root.title("SPACE WAR")
root.resizable(False,False)
root.bind("<Key>",move)
cvs = tkinter.Canvas(width=WIDTH,height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="universe.png")
player=tkinter.PhotoImage(file="player.png")
enemy=tkinter.PhotoImage(file="enemy.png")
main()
root.mainloop()
