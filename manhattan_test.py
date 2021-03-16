import manhattan
import sys
import argparse


def test_1(capsys):

    parser = argparse.ArgumentParser()
    parser.add_argument('x1')
    parser.add_argument('y1')
    parser.add_argument('x2')
    parser.add_argument('y2')
    args = parser.parse_args(['5', '4', '3', '2'])

    manhattan.main(args)

    out, err = capsys.readouterr()

    assert out == "Distance between A and B is: 4\n"
    assert err == ""


def test_2(capsys):

    parser = argparse.ArgumentParser()
    parser.add_argument('x1')
    parser.add_argument('y1')
    parser.add_argument('x2')
    parser.add_argument('y2')
    args = parser.parse_args(['-1', '2', '1', '-2'])

    manhattan.main(args)

    out, err = capsys.readouterr()

    assert out == "Distance between A and B is: 6\n"
    assert err == ""

def test_3(capsys):

    parser = argparse.ArgumentParser()
    parser.add_argument('x1')
    parser.add_argument('y1')
    parser.add_argument('x2')
    parser.add_argument('y2')
    args = parser.parse_args(['0', '0', '0', '0'])

    manhattan.main(args)

    out, err = capsys.readouterr()

    assert out == "Distance between A and B is: 0\n"
    assert err == ""

def test_4(capsys):

    parser = argparse.ArgumentParser()
    parser.add_argument('x1')
    parser.add_argument('y1')
    parser.add_argument('x2')
    parser.add_argument('y2')
    args = parser.parse_args(['-1', '2', '1', 'r'])

    manhattan.main(args)

    out, err = capsys.readouterr()

    assert out == ""
    assert err == "Cannot parse arguments as integers\n"
