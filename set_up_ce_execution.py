from controllers import database_controller, collection_instrument_controller

if __name__ == '__main__':
    collection_instrument_controller.load_collection_instrument_bricks_201801()
    database_controller.reset_rm_database('resources/database/set_up_ce_execute.sql')
