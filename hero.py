import random
import math
import enemy
import sys
class human:
    """大体共通するクラス"""
    def __init__(self,name,job,hp,mp,n_attack):
        self.name=name
        self.job=job
        self.max_hp=hp
        self.hp=hp
        self.max_mp=mp
        self.mp=mp
        self.n_attack=n_attack
        self.power=1
        self.power_turn=0
        self.cri_up_turn=0
        self.poison=0
        self.mahi=0
        self.blood=0

    def show(self):
        print("\n名前:{} | 職業:{} | hp:{}/{} | mp:{}/{} |".format(self.name,self.job,self.hp,self.max_hp,self.mp,self.max_mp))

    def check(self):
        if self.poison>0:
            self.poison_status()
        else:
            pass
    def remaing_hp(self,damage):
        self.hp-=damage
        print("\n{}は{}のダメージをうけた\n".format(self.name,damage))
        if self.hp<=0:
            print("死んだ")
            sys.exit()


    def remaing_mp(self,used_mp):
        self.mp-=used_mp
    def charge_hp(self,care_hp):
        if self.hp<self.max_hp:
            self.hp+=care_hp
            print("\n{}は\nhpを{}回復した\n".format(self.name,care_hp))
            if self.hp>self.max_hp:
                self.hp=self.max_hp
        else:
            print("これ以上回復できない")
    def charge_mp(self,care_mp):
        if self.mp<self.max_mp:
            self.mp+=care_mp
            print("\n{}は\nmpを{}回復した\n".format(self.name,care_mp))
            if self.mp>self.max_mp:
                self.mp=self.max_mp
        else:
            print("これ以上回復できない")
    def poison_status(self):
        self.remaing_hp(15)
        self.poison-=1
        print("毒で15のダメージ")

        if self.hp<=0:
            print("死んだ")
            sys.exit()


    def receive_poison(self,poison_turn):
        self.poison=poison_turn
    def base_attack(self,trick):
        self.power_status(self.power_turn)
        if self.cri_up_turn>0:
            self.cri=random.randint(1,10)
            if self.cri>3:
                self.cri_rate=1.4
            else:
                self.cri_rate=1
            self.cri_up_turn-=1
        else:
            self.cri=random.randint(1,10)
            if self.cri>8:
                self.cri_rate=1.4
            else:
                self.cri_rate=1
        attack_value=math.floor(trick*self.cri_rate*self.power)
        enemy.ene.remaing_hp(attack_value)

    def power_status(self,power_turn):
        self.power_turn=power_turn
        if self.power_turn>0:
            self.power=1.5
            self.power_turn-=1
        elif self.power_turn<0:
            self.power=0.5
            self.power_turn+=1
        else:
            self.power=1



    def next_do(self):
        while True:
            try:
                do=int(input("1:攻撃　2:アイテム　3:特技　4:ステータス\n"))
                if do>4 and do<=0:
                    print("入力し直し")
                elif do>0 and do<5:
                    break
                else:
                    print("入力し直し")
            except:
                print("入力し直し")
        if do==1:
            self.base_attack(self.n_attack)
        elif do==2:
            item.choice_item(self.name)
        elif do==3:
            self.special()
        elif do==4:
            show_status().show_info(self.name)


class show_status:
    def show_info(self,name):
        self.name=name
        man2.show()
        enemy.ene.show()
        if self.name=="man":
            self.name=man2
        self.name.next_do()

class Item:
    def __init__(self):
        self.hp_recover=10
        self.mp_recover=10
        self.gedoku=10
        self.siketu=10
        self.itamidome=10
    def choiced_hp_recover(self):
        if self.hp_recover>0:
            self.name.charge_hp(50)
            self.hp_recover-=1
        else:
            print("薬がない")
            self.choice_item(self.name)
    def choiced_mp_recover(self):
        if self.mp_recover>0:
            self.name.charge_mp(50)
            self.mp_recover-=1
        else:
            print("薬がない")
            self.choice_item(self.name)
    def choiced_gedoku(self):
        if self.gedoku>0:
            self.name.receive_poison(0)
        else:
            print("薬がない")
            self.choice_item(self.name)
    def choiced_siketu(self):
        pass
    def choiced_itamidome(self):
        pass
    def choice_item(self,name):
        if name=="man":
            self.name=man2
        while True:
            try:
                choice=int(input("1:hp回復薬 {} |2:mp回復薬 {} |3:解毒剤 {} |4:戻る".format(self.hp_recover,self.mp_recover,self.gedoku)))
                if choice>4 and choice<1:
                    print("やり直し")
                else:
                    break
            except:
                print("やり直し")
        if choice==1:
            self.choiced_hp_recover()
        elif choice==2:
            self.choiced_mp_recover()
        elif choice==3:
            self.choiced_gedoku()
        elif choice==4:
            self.name.next_do()

class man(human):
    def do_power_up(self):
        if self.mp>0:
            self.remaing_mp(10)
            self.power_status(5)
            print("強化した\n")
        else:
            print("mpが足りない!")

    def strong_attack(self):
        if self.mp>0:
            self.remaing_mp(5)
            self.base_attack(50)
        else:
            print("mpが足りない!")

    def critical_up(self):
        if self.mp>0:
            self.remaing_mp(10)
            self.cri_up_turn=5
            print("集中した\n")
        else:
            print("mpが足りない!")

    def special(self):
        while True:
            try:
                do=int(input("1:強化　2:強攻撃　3:集中　4:戻る\n"))
                if do>4 and do<=0:
                    print("入力し直し")
                elif do>0 and do<5:
                    break
                else:
                    print("入力し直し")
            except:
                print("入力し直し")
        if do==1:
            self.do_power_up()
        elif do==2:
            self.strong_attack()
        elif do==3:
            self.critical_up()
        else:
            self.next_do()

item=Item()
man2=man("man","デバック",300,300,30)
