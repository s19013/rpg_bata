import random
import math
import hero
import sys
class Enemy:
    """敵のクラス"""
    def __init__(self,name,hp,n_attack):
        self.name=name
        self.max_hp=hp
        self.hp=hp
        self.n_attack=n_attack
        self.power=1
        self.power_turn=0
        self.cri_up_turn=0
        self.poison=0
        self.mahi=0
        self.blood=0
    def show(self):
        print("\n名前:{} |hp:{}/{}".format(self.name,self.hp,self.max_hp))
    def die(self):
        return True

    def remaing_hp(self,damage):
        self.hp-=damage
        print("\n{}は{}のダメージをうけた\n".format(self.name,damage))
        if self.hp<=0:
            print("敵を倒した")
            sys.exit()

    def charge_hp(self,care_hp):
        if self.hp<self.max_hp:
            self.hp+=care_hp
            print("\n{}は\nhpを{}回復した\n".format(self.name,care_hp))
            if self.hp>self.max_hp:
                self.hp=self.max_hp
        else:
            print("これ以上回復できない")

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
        hero.man2.remaing_hp(attack_value)

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

    def do_power_up(self):
        self.power_status(5)
        print("ene 強化した\n")

    def week(self):
        print("ene 弱体化した")

    def poison_attack(self):
        hero.man2.receive_poison(3)
        print("ene 毒攻撃")

    def enemy_do(self):
        if self.hp>(self.max_hp/2):
            do=random.randint(1,100)
            if do<=40:
                self.base_attack(self.n_attack)
            elif 40<do<=60:
                strong=self.n_attack*2
                self.base_attack(strong)
            elif 60<do<=70:
                self.do_power_up()
            elif 70<do<=80:
                self.week()
            elif 80<do<=90:
                if self.hp<100:
                    self.charge_hp(50)
                else:
                    self.enemy_do()
            else:
                self.poison_attack()
        else:
            do=random.randint(1,100)
            if do<=30:
                self.base_attack(self.n_attack)
            elif 30<do<=60:
                strong=self.n_attack*2
                self.base_attack(strong)
            elif 60<do<=70:
                self.do_power_up()
            elif 70<do<=80:
                self.week()
            elif 80<do<=90:
                if self.hp<100:
                    self.charge_hp(50)
                else:
                    self.base_attack(self.n_attack)
            else:
                self.poison_attack()

ene=Enemy("ene1",300,30)
