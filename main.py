from ThreeKingdom.basic import *
import time
import logging


if __name__ == '__main__':
    game = Battle()
    city = MainCity()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(lineno)d: %(message)s\n', filemode='a',
                        datefmt='%Y-%m-%d(%a)%H:%M:%S', filename='./log.txt')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger().addHandler(console)

    logging.info("init finished")
    iter_time = 0
    while (game.map == 1).sum() > 0:
        iter_time += 1
        logging.info("iter {}, unconquer map number: {}".format(iter_time, (game.map == 1).sum()))

        next_inds = find_nearest(game.cur_center_location, game.map)
        logging.info("next inds: x {}, y {}".format(next_inds[0], next_inds[1]))

        game.move(game.cur_center_location[0], game.cur_center_location[1], next_inds[0], next_inds[1])
        logging.info("move finished")

        attack_return = game.attack("center")
        logging.info("attack finished")

        if attack_return == "no army":
            game.back()
            logging.info("no army, wait")
            game.delay(60*1000*7)
            logging.info("back to center")
            game.attack_module.army.back_main_city()

            logging.info("entry center")
            city.entry()

            city.build()
            logging.info("build finished")

            game.attack_module.army.conscription()
            logging.info("army conscription finished")

            game.attack_module.army.re_allocate()
            logging.info("army re_allocate finished")

            game.back()
            game.init_window()
            logging.info("init window finished")








