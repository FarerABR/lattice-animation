from manim import *


class LatticeScene(Scene):
    def construct(self):
        self.wait(1)

        # Define basis vectors
        v1 = np.array([1, 0, 0])
        v2 = np.array([0, 1, 0])

        # Draw basis arrows
        basis1 = Arrow(ORIGIN, v1, buff=0, color=BLUE)
        basis2 = Arrow(ORIGIN, v2, buff=0, color=GREEN)
        label1 = MathTex("\mathbf{v}_1").next_to(basis1.get_end(), DOWN)
        label2 = MathTex("\mathbf{v}_2").next_to(basis2.get_end(), RIGHT)

        self.play(GrowArrow(basis1), Write(label1))
        self.play(GrowArrow(basis2), Write(label2))

        # Generate lattice points
        points = VGroup()
        pts = list()
        for i in range(-10, 10):
            for j in range(-10, 10):
                pt = Dot(point=np.array([i, j, 0]), radius=0.06, color=YELLOW)
                pt.i = i
                pt.j = j
                pts.append(np.array([i, j, 0]))
                points.add(pt)

        # Animate lattice appearance
        self.play(
            LaggedStartMap(FadeIn, points, shift=DOWN, lag_ratio=0.02), run_time=0.8
        )
        self.wait(2)

        v3 = np.array([1.54, 0.22, 0])
        v4 = np.array([2.39, 0.88, 0])
        basis3 = Arrow(ORIGIN, v3, buff=0, color=BLUE)
        basis4 = Arrow(ORIGIN, v4, buff=0, color=GREEN)
        label3 = MathTex("\mathbf{v}_1").next_to(basis3.get_end(), DOWN)
        label4 = MathTex("\mathbf{v}_2").next_to(basis4.get_end(), RIGHT)

        animations = []
        ani2 = []
        for pt in points:
            new_pos = pt.i * v3 + pt.j * v4
            animations.append(pt.animate.move_to(new_pos))

        self.play(
            Transform(basis1, basis3),
            Transform(label1, label3),
            Transform(basis2, basis4),
            Transform(label2, label4),
            *animations,
            run_time=1
        )
        # self.play(*animations)   
        self.wait(2)

        i = 0
        for pt in points:
            ani2.append(pt.animate.move_to(pts[i]))
            i += 1

        self.play(
            Transform(basis1, Arrow(ORIGIN, v1, buff=0, color=BLUE)),
            Transform(basis2, Arrow(ORIGIN, v2, buff=0, color=YELLOW)),
            Transform(label1, MathTex("\mathbf{v}_1").next_to(v1, DOWN)),
            Transform(label2, MathTex("\mathbf{v}_2").next_to(v2, RIGHT)),
            *ani2,
            run_time=1
        )
        dt = Dot(point=np.array([1, 3, 0]), radius=0.06, color=YELLOW_E)
        self.add(dt)
        self.wait(1)

        self.play(
            FadeOut(basis1),
            FadeOut(basis2),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(points),
        )

        # Setup plane
        plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.5},
        )
        lbl = MathTex("(1,3)").next_to(np.array([1, 3, 0]), UP)
        self.play(FadeIn(plane), Write(lbl), run_time=0.5)
        self.wait(1)

        ar11 = Arrow(ORIGIN, np.array([1, 0, 0]), buff=0, color=BLUE)
        ar22 = Arrow(ar11.end, np.array([1, 1, 0]), buff=0, color=YELLOW)
        ar33 = Arrow(ar22.end, np.array([1, 2, 0]), buff=0, color=YELLOW)
        ar44 = Arrow(ar33.end, np.array([1, 3, 0]), buff=0, color=YELLOW)

        self.play(GrowArrow(ar11), run_time=0.4)
        self.play(GrowArrow(ar22), run_time=0.4)
        self.play(GrowArrow(ar33), run_time=0.4)
        self.play(GrowArrow(ar44), run_time=0.4)
        self.wait(2)

        self.play(FadeOut(ar11), FadeOut(ar22), FadeOut(ar33), FadeOut(ar44))

        # Define basis vectors
        v3 = np.array([3, 1, 0])
        v4 = np.array([5, 3, 0])

        # Draw basis arrows
        basis3 = Arrow(ORIGIN, v3, buff=0, color=RED)
        basis4 = Arrow(ORIGIN, v4, buff=0, color=GREEN)
        label3 = MathTex("\mathbf{v}_3").next_to(basis3.get_end(), UP)
        label4 = MathTex("\mathbf{v}_4").next_to(basis4.get_end(), UP)

        self.play(GrowArrow(basis3), Write(label3))
        self.play(GrowArrow(basis4), Write(label4))
        self.wait(2)

        self.play(FadeOut(basis3), FadeOut(basis4), FadeOut(label3), FadeOut(label4))

        self.play(FadeIn(ar11), FadeIn(ar22), FadeIn(ar33), FadeIn(ar44))

        ar1 = Arrow(ORIGIN, -v3, buff=0, color=RED)
        ar2 = Arrow(ar1.end, np.array([-6, -2, 0]), buff=0, color=RED)
        ar3 = Arrow(ar2.end, np.array([-1, 1, 0]), buff=0, color=GREEN)
        ar4 = Arrow(ar3.end, np.array([4, 4, 0]), buff=0, color=GREEN)
        ar5 = Arrow(ar4.end, np.array([1, 3, 0]), buff=0, color=RED)
        self.play(GrowArrow(ar1), run_time=0.4)
        self.play(GrowArrow(ar2), run_time=0.4)
        self.play(GrowArrow(ar3), run_time=0.4)
        self.play(GrowArrow(ar4), run_time=0.4)
        self.play(GrowArrow(ar5), run_time=0.4)
        self.wait(2)

        self.play(
            FadeOut(ar1),
            FadeOut(ar2),
            FadeOut(ar3),
            FadeOut(ar4),
            FadeOut(ar5),
            FadeOut(ar11),
            FadeOut(ar22),
            FadeOut(ar33),
            FadeOut(ar44),
            FadeOut(dt),
            FadeOut(lbl),
            FadeOut(plane),
        )

        # LWE

        dt2 = Dot(point=np.array([-2, 1, 0]), radius=0.06, color=YELLOW_E)
        dt3 = Dot(point=np.array([-2.56, 1.475, 0]), radius=0.06, color=BLUE)
        self.play(GrowArrow(basis1), Write(label1), GrowArrow(basis2), Write(label2))

        self.play(FadeIn(dt2))
        self.wait(1)
        self.play(FadeIn(dt3))
        self.wait(2)
        self.play(FadeOut(basis1), FadeOut(basis2), FadeOut(label1), FadeOut(label2))

        arw1 = Arrow(ORIGIN, np.array([-1, 0, 0]), buff=0, color=BLUE)
        arw2 = Arrow(arw1.end, [-2, 0, 0], buff=0, color=BLUE)
        arw3 = Arrow(arw2.end, [-3, 0, 0], buff=0, color=BLUE)
        arw4 = Arrow(arw3.end, [-3, 1, 0], buff=0, color=YELLOW)
        self.play(GrowArrow(arw1), run_time=0.4)
        self.play(GrowArrow(arw2), run_time=0.4)
        self.play(GrowArrow(arw3), run_time=0.4)
        self.play(GrowArrow(arw4), run_time=0.4)
        dt4 = Dot(point=np.array([-3, 1, 0]), radius=0.06, color=RED)
        lbl2 = MathTex("(-2,1)").next_to(np.array([-2, 1, 0]), RIGHT)
        lbl3 = MathTex("(-2.56,1.475)").next_to(np.array([-2.56, 1.475, 0]), UP)
        lbl4 = MathTex("(-3,1)").next_to(np.array([-3, 1, 0]), LEFT)
        self.play(FadeIn(dt4))
        self.play(Write(lbl2), Write(lbl3), Write(lbl4), run_time=0.5)

        self.wait(2)
        # self.play(
        #     FadeOut(lbl2),
        #     FadeOut(lbl3),
        #     FadeOut(lbl4),
        #     FadeOut(dt2),
        #     FadeOut(dt4),
        #     FadeOut(arw1),
        #     FadeOut(arw2),
        #     FadeOut(arw3),
        #     FadeOut(arw4),
        #     run_time=0.1,
        # )

class ThreeDScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
                
        # Set up the 3D axes
        axes = ThreeDAxes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            z_range=[-10, 10, 1],
            axis_config={"color": GRAY, "stroke_width": 0.5},
        )

        # Create a point in 3D space
        point = Dot3D(point=np.array([1, 2, 3]), radius=0.1, color=YELLOW)

        # Create a label for the point
        label = MathTex("P(1,2,3)").next_to(point, UP)

        # Add the axes and point to the scene
        self.add(axes, point, label)

        # Rotate the camera around the axes
        self.wait(2)