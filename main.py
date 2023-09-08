# 配置导入库目录
import sys
import os
import traci
sys.path.append("C:\\Program Files (x86)\\Eclipse\\Sumo\\tools")
#配置调用目录
sumoBinary = "C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo-gui"
# sumoCmd = [sumoBinary, "-c", "C:\\Program Files (x86)\\Eclipse\\Sumo\\tools\\game\\square.sumocfg"]
sumoCmd = [sumoBinary, "-c", "C:/users/luolan/Sumo/2023-09-07-17-05-17/guangdonggongyedaxue.sumocfg"]

def generate_routefile():
    random.seed(42)  # make tests reproducible
    N = 3600  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    with open("C:/users/luolan/Sumo/2023-09-07-17-05-17/cross.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" \
guiShape="passenger"/>
        <vType id="typeNS" accel="0.8" decel="4.5" sigma="0.5" length="7" minGap="3" maxSpeed="25" guiShape="bus"/>

        <route id="right" edges="51o 1i 2o 52i" />
        <route id="left" edges="52o 2i 1o 51i" />
        <route id="down" edges="54o 4i 3o 53i" />""", file=routes)
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="right_%i" type="typeWE" route="right" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="left_%i" type="typeWE" route="left" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="down_%i" type="typeNS" route="down" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
        print("</routes>", file=routes)



traci.start(sumoCmd)

step = 0
while step < 1000:
   traci.simulationStep()
   step += 1

traci.close()











# 导入traci模块
import traci
#
#
# traci.start(sumoCmd)
#
#
# step = 0
# isAdd = True
#
# while step < 3000:
#     traci.simulationStep()
#     current_time = traci.simulation.getTime()
#     IDlist = traci.vehicle.getIDList()
#     if step % 10 == 0:
#         print("----------------")
#         for Id in IDlist:
#             print('车辆', Id, ':', traci.vehicle.traci.vehicle.getSpeed(Id))
#             print('车辆', Id, ':', traci.vehicle.getPosition3D(Id))
#             print("***********************")
#             # traci.vehicle.setParameter(Id, "maxSpeed", 20.0)
#             # speed = traci.vehicle.getSpeed(Id)  # 获取车辆速度
#             # position = traci.vehicle.getPosition(Id)  # 获取车辆位置
#             # new_speed = 10.0  # 新的速度值
#             # traci.vehicle.setSpeed(Id, new_speed)
#             # print('车辆', Id, ':', traci.vehicle.traci.vehicle.getSpeed(Id))
#             # print('车辆', Id, ':', traci.vehicle.getPosition3D(Id))
#             # print("------------------------------------------------")
#
#
#
#
#         # 获取编号为0的车辆路线id
#         # trip000= traci.vehicle.getRouteID("0")
#         # 添加路线，编号为trip000，路线包含边 rightoto1/0’，'1/0to1/1’，1/1tonight1
#         # traci.route.add("trip000", ['right0to1/0', '1/0to1/1', '1/1tonight1'])
#         #输出编号“0”的车辆路线
#         # print(traci.vehicle.getRoute("0"))
#         # 添加车辆，车辆id为"newVeh"，沿路线 “trip000"行驶
#         # traci.vehicle.add("newVeh","trip000")
#
#         # 设置"newVeh"的速度
#         # traci.vehicle.setDecel("newVeh",10)
#         #设置"newVeh"的颜色，暂未起作用
#         # colora = (125,255,255,255)
#         # traci.vehicle.setColor("newVeh", colora)
#         #设置"newVeh"的长度
#         # traci.vehicle .setLength("newVeh",10)
#         # 获取"newVeh"当前位置
#         # print(traci.vehicle.getPosition3D("newVeh"))
#     step += 1
# # traci.close()