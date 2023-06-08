"""
An example of how to use the class RTSys
"""
import argparse
import pyhydrophone as pyhy

Vpp = 2.0


def main(filepath):
    # Hydrophone Setup
    sensitivity = -180
    preamp_gain = 0
    model = 1
    serial_number = 1000
    name = 'RESEA320'
    mode = 'lowpower'

    rtsys = pyhy.RTSys(name, model, serial_number, sensitivity, preamp_gain, Vpp, mode)
    rtsys.plot_consumption_total_mission(mission_folder_path=filepath)
    print('Total consumption', rtsys.compute_consumption_total_mission(mission_folder_path=filepath))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot the power consumption of the mission folder')
    parser.add_argument('board_path', type=str, nargs='+', help='Path to the mission folder')
    args = parser.parse_args()
    board_path = args.board_path[1]
    main(board_path)
