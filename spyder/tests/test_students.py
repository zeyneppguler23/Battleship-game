import importlib
import inspect

import pytest
import tests.test_helper_functions as thf

testReport = thf.TestReport("test_report.txt")


########################################################################################################################
# Test Components.py functions
########################################################################################################################
@pytest.mark.depends()
def test_components_exists():
    """
    Test if the components module exists.
    """
    try:
        importlib.import_module('components')
    except ImportError:
        testReport.add_message("components module does not exist in your solution.")
        pytest.fail("components module does not exist")


@pytest.mark.depends(on=["test_components_exists"])
def test_initialise_board_exists():
    """
    Test if the initialise_board function exists.
    """
    components = importlib.import_module('components')

    try:
        assert hasattr(components, 'initialise_board'), "initialise_board function does not exist"
    except AssertionError:
        testReport.add_message("initialise_board function does not exist in your solution.")
        pytest.fail("initialise_board function does not exist")


@pytest.mark.depends(on=["test_components_exists"])
def test_initialise_board_argument():
    """
    Test if the initialise_board function accepts an integer argument.
    """
    components = importlib.import_module('components')

    try:
        components.initialise_board(10)
    except TypeError:
        testReport.add_message("initialise_board function does not accept an integer argument")
        pytest.fail("initialise_board function does not accept an integer argument")
    except Exception as e:
        testReport.add_message("test_initialise_board_argument failed as the function threw an unexpected error. ("
                               "Crashed before test completed) Check the test output window for details")
        pytest.fail("test_initialise_board_argument failed as the function threw an unexpected error. ")


@pytest.mark.depends(on=["test_components_exists"])
def test_initialise_board_return_type():
    """
    Test if the initialise_board function returns a list.
    """
    components = importlib.import_module('components')

    try:
        assert thf.is_list_of_lists(components.initialise_board(10), str)
    except AssertionError:
        testReport.add_message("initialise_board function does not return the correct datatype"
                               "Your initialise board function should return a list of lists of either strings or "
                               "None values")
        pytest.fail("initialise_board function does not return a list")
    except Exception:
        testReport.add_message("test_initialise_board_type failed as the function initialise_board threw an "
                               "unexpected error. ("
                               "Crashed before test completed) Check the test output window for details")
        pytest.fail("test_initialise_board_argument failed as the function threw an unexpected error. ")


@pytest.mark.depends(on=["test_components_exists"])
def test_create_battleships_exists():
    """
    Test if the create_battleships function exists.
    """
    components = importlib.import_module('components')

    try:
        assert hasattr(components, 'create_battleships'), "create_battleships function does not exist"
    except AssertionError:
        testReport.add_message("create_battleships function does not exist in your solution.")
        pytest.fail("create_battleships function does not exist")


def test_battleships_txt_exists():
    """
    Test if the battleships.txt file exists.
    """
    try:
        open("battleships.txt", "r")
    except FileNotFoundError:
        open("battleships_temp.txt", "w")
        testReport.add_message("battleships.txt file does not exist in your solution. "
                               "A file called battleships_temp.txt has been created in the expected location. "
                               "Please rename this file to battleships.txt and add your battleships to it.")
        pytest.fail("battleships.txt file does not exist")


@pytest.mark.depends(on=["test_components_exists", "test_battleships_txt_exists"])
def test_create_battleships_argument():
    """
    Test if the create_battleships function accepts a string argument.
    """
    components = importlib.import_module('components')

    try:
        components.create_battleships("battleships.txt")
    except TypeError:
        testReport.add_message("create_battleships function does not accept a string argument")
        pytest.fail("create_battleships function does not accept a string argument")
    except Exception:
        testReport.add_message("test_create_battleships_argument failed as the function create_battleships"
                               " threw an unexpected error. ("
                               "Crashed before test completed) Check the test output window for details")
        pytest.fail("test_create_battleships_argument failed as the function threw an unexpected error. ")


@pytest.mark.depends(on=["test_components_exists", "test_battleships_txt_exists"])
def test_create_battleships_return_type():
    """
    Test if the create_battleships function returns a dictionary.
    """
    components = importlib.import_module('components')

    try:
        assert thf.is_dict_of_type(components.create_battleships("battleships.txt"), str, int)
    except AssertionError:
        testReport.add_message("create_battleships function does not return a dictionary")
        pytest.fail("create_battleships function does not return a dictionary")
    except Exception:
        testReport.add_message("test_create_battleships_return_type failed as the function create_battleships"
                               " threw an unexpected error. ("
                               "Crashed before test completed) Check the test output window for details")
        pytest.fail("test_create_battleships_return_type failed as the function threw an unexpected error. ")


@pytest.mark.depends(on=["test_components_exists"])
def test_place_battleships_exists():
    """
    Test if the place_battleships function exists.
    """
    components = importlib.import_module('components')

    try:
        assert hasattr(components, 'place_battleships'), "place_battleships function does not exist"
    except AssertionError:
        testReport.add_message("place_battleships function does not exist in your solution.")
        pytest.fail("place_battleships function does not exist")


@pytest.mark.depends(on=["test_components_exists", "test_battleships_txt_exists"])
def test_place_battleships_arguments():
    """
    Test if the place_battleships function accepts a list and a dictionary argument.
    """
    components = importlib.import_module('components')

    try:
        # Check to make sure the place_battleships function has a board ships and algorithm argument
        assert "board" in inspect.signature(components.place_battleships).parameters, ("place_battleships function"
                                                                                       "does not have a board argument")
        assert "ships" in inspect.signature(components.place_battleships).parameters, ("place_battleships function "
                                                                                       "does not have a ships argument")
        assert "algorithm" in inspect.signature(components.place_battleships).parameters, ("place_battleships function "
                                                                                           "does not have a algorithm "
                                                                                           "argument")
    except AssertionError:
        testReport.add_message("place_battleships function is missing an argument."
                               "Check your function has a board, ships and algorithm argument")
        pytest.fail("place_battleships function does not have a board, ships and algorithm argument")
    except Exception:
        testReport.add_message("test_place_battleships_arguments failed as one of the functions place_battleships, "
                               "initialise_board or create_battleships"
                               " threw an unexpected error. ("
                               "Crashed before test completed) Check the test output window for details")
        pytest.fail("test_place_battleships_arguments failed as the function threw an unexpected error. ")

    try:
        board = components.initialise_board(10)
        ships = components.create_battleships("battleships.txt")
        components.place_battleships(board, ships)
    except TypeError:
        testReport.add_message("place_battleships function does not accept a list (board) and a dictionary argument")
        pytest.fail("place_battleships function does not accept a list and a dictionary argument")
    except Exception:
        testReport.add_message("test_place_battleships_arguments failed as one of the functions place_battleships, "
                               "initialise_board or create_battleships"
                               " threw an unexpected error. ("
                               "Crashed before test completed) Check the test output window for details")
        pytest.fail("test_place_battleships_arguments failed as the function threw an unexpected error. ")


@pytest.mark.depends(on=["test_components_exists", "test_battleships_txt_exists"])
def test_place_battleships_return_type():
    """
    Test if the place_battleships function returns a list of lists of strings/None values.
    """
    components = importlib.import_module('components')

    board = components.initialise_board(10)
    ships = components.create_battleships("battleships.txt")
    try:
        assert thf.is_list_of_lists(components.place_battleships(board, ships), str), ("place_battleships function "
                                                                                       "does not return a list of "
                                                                                       "lists of strings/None values")
    except AssertionError:
        testReport.add_message("place_battleships function does not return a list of lists of strings or None values"
                               " The returned board should only contain None or ship names")
        pytest.fail("place_battleships function does not return a list of lists of list of strings/None")
    except Exception:
        testReport.add_message("test_place_battleships_return_type failed as one of the functions place_battleships, "
                               "initialise_board or create_battleships"
                               " threw an unexpected error. ("
                               "Crashed before test completed)  Check the test output window for details")
        pytest.fail("test_place_battleships_return_type failed as the function threw an unexpected error. ")


########################################################################################################################
# Test Game Engine.py functions
########################################################################################################################

@pytest.mark.depends()
def test_game_engine_exists():
    """
    Test if the game_engine module exists.
    """
    try:
        importlib.import_module('game_engine')
    except ImportError:
        testReport.add_message("game_engine module does not exist in your solution.")
        pytest.fail("game_engine module does not exist")


@pytest.mark.depends(on=["test_game_engine_exists"])
def test_attack_exists():
    """
    Test if the attack function exists.
    """
    try:
        game_engine = importlib.import_module('game_engine')
        assert hasattr(game_engine, 'attack'), "attack function does not exist"
    except AssertionError:
        testReport.add_message("attack function does not exist in your solution.")
        pytest.fail("attack function does not exist")


@pytest.mark.depends(on=["test_game_engine_exists", "test_components_exists", "test_battleships_txt_exists"])
def test_attack_arguments():
    """
    Test if the attack function accepts a tuple, a list, and a dictionary argument.
    """
    try:
        components = importlib.import_module('components')
        game_engine = importlib.import_module('game_engine')
        coordinates = (1, 1)
        board = components.initialise_board(10)
        battleships = components.create_battleships("battleships.txt")
        game_engine.attack(coordinates, board, battleships)
    except TypeError:
        testReport.add_message("attack function does not accept a tuple, a list, and a dictionary argument")
        pytest.fail("attack function does not accept a tuple, a list, and a dictionary argument")
    except Exception:
        testReport.add_message("test_attack_arguments failed as one of the functions place_battleships, "
                               "initialise_board or create_battleships or attack"
                               " threw an unexpected error. ("
                               "Crashed before test completed). Check the test output window for deatils")
        pytest.fail("test_attack_arguments failed as one of the functions place_battleships, "
                    "initialise_board or create_battleships or attack"
                    " threw an unexpected error. ("
                    "Crashed before test completed).")


@pytest.mark.depends(on=["test_game_engine_exists"])
def test_cli_coordinates_input_exists():
    """
    Test if the cli_coordinates_input function exists.
    """
    try:
        game_engine = importlib.import_module('game_engine')
        assert hasattr(game_engine, 'cli_coordinates_input'), "cli_coordinates_input function does not exist"
    except AssertionError:
        testReport.add_message("cli_coordinates_input function does not exist in your solution.")
        pytest.fail("cli_coordinates_input function does not exist")


@pytest.mark.depends(on=["test_game_engine_exists"])
def test_simple_game_loop_exists():
    """
    Test if the simple_game_loop function exists.
    """
    try:
        game_engine = importlib.import_module('game_engine')
        assert hasattr(game_engine, 'simple_game_loop'), "simple_game_loop function does not exist"
    except AssertionError:
        testReport.add_message("simple_game_loop function does not exist in your solution.")
        pytest.fail("simple_game_loop function does not exist")


########################################################################################################################
# Test mp_game_engine.py functions
########################################################################################################################

@pytest.mark.depends()
def test_mp_game_engine_exists():
    """
    Test if the mp_game_engine module exists.
    """
    try:
        importlib.import_module('mp_game_engine')
    except ImportError:
        testReport.add_message("mp_game_engine module does not exist in your solution.")
        pytest.fail("mp_game_engine module does not exist")


@pytest.mark.depends(on=["test_mp_game_engine_exists"])
def test_generate_attack_exists():
    """
    Test if the generate_attack function exists.
    """
    try:
        mp_game_engine = importlib.import_module('mp_game_engine')
        assert hasattr(mp_game_engine, 'generate_attack'), "generate_attack function does not exist"
    except AssertionError:
        testReport.add_message("generate_attack function does not exist in your solution.")
        pytest.fail("generate_attack function does not exist")


@pytest.mark.depends(on=["test_mp_game_engine_exists"])
def test_generate_attack_return_type():
    """
    Test if the generate_attack function returns a tuple.
    """
    try:
        mp_game_engine = importlib.import_module('mp_game_engine')
        assert isinstance(mp_game_engine.generate_attack(), tuple)
    except AssertionError:
        testReport.add_message("generate_attack function does not return a tuple")
        pytest.fail("generate_attack function does not return a tuple")


@pytest.mark.depends(on=["test_mp_game_engine_exists"])
def test_ai_opponent_game_loop_exists():
    """
    Test if the ai_opponent_game_loop function exists.
    """
    try:
        mp_game_engine = importlib.import_module('mp_game_engine')
        assert hasattr(mp_game_engine, 'ai_opponent_game_loop'), "ai_opponent_game_loop function does not exist"
    except AssertionError:
        testReport.add_message("ai_opponent_game_loop function does not exist in your solution.")
        pytest.fail("ai_opponent_game_loop function does not exist")


########################################################################################################################
# Test main.py functions
########################################################################################################################
@pytest.mark.depends()
def test_main_module_exists():
    """
    Test if the main module exists.
    """
    try:
        importlib.import_module('main')
    except ImportError:
        testReport.add_message("main module does not exist in your solution.")
        pytest.fail("main module does not exist")


@pytest.mark.depends(on=["test_main_module_exists"])
def test_root_exists():
    """
    Test if the root function exists.
    """
    try:
        main_module = importlib.import_module('main')
        assert hasattr(main_module, 'root'), "root function does not exist"
    except AssertionError:
        testReport.add_message("root function does not exist in your solution.")
        pytest.fail("root function does not exist")


@pytest.mark.order(after="test_second")
@pytest.mark.depends(on=["test_root_exists"])
def test_attack_exists():
    """
    Test if the attack function exists.
    """
    try:
        main_module = importlib.import_module('main')
        assert hasattr(main_module, 'process_attack'), "process_attack function does not exist"
    except AssertionError:
        testReport.add_message("process_attack function does not exist in your solution.")
        pytest.fail("process_attack function does not exist")


@pytest.mark.depends(on=["test_main_module_exists"])
def test_placement_interface_exists():
    """
    Test if the placement_interface function exists.
    """
    try:
        main_module = importlib.import_module('main')
        assert hasattr(main_module, 'placement_interface'), "placement_interface function does not exist"
    except AssertionError:
        testReport.add_message("placement_interface function does not exist in your solution.")
        pytest.fail("placement_interface function does not exist")
