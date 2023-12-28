Feature: Point Conversion

    Scenario: Convert Cartesian coordinates to polar coordinates
        Given a Cartesian point with x-coordinate 3 and y-coordinate 4
        When converting the Cartesian point to polar coordinates
        Then the resulting coordinates should be x: 3, y: 4

    Scenario: Convert polar coordinates to Cartesian coordinates
        Given a polar point with radius 1 and angle 2 degrees
        When converting the polar point to Cartesian coordinates
        Then the resulting Cartesian coordinates should be x: -0.4161468365471424, y: 0.9092974268256817

