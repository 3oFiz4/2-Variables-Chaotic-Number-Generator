# **CIFRE (Chaotic Inverse Fractional Reverse Exponential)**
This is a random code I made in the middle 10 PM to be able to generate a random chaotic number between two variables. This code has no purpose. It my daily way to assert intellectual quirk over nobody. :D

It is called, **CIFRE (Chaotic Inverse Fractional Reverse Exponential)** _im too creative with the name_

Can be represented as:<br/>
$\zeta(a,b) = \sum_{i=1}^{n} \left(\frac{a_{2(i-1)}}{b_{2(i-1)}}\right)^{-\frac{b}{a}}, \quad b_0 = \left(\frac{a}{b}\right)^{\frac{b}{a}}, \quad a_0 = b_0^{-1}$

The whole process of the algorithm can be expressed such that:<br/>
$$c = a \times b $$<br/>
$$T_0 = 0$$<br/>
$$b_2 = \left(\frac{a}{b}\right)^{\frac{b}{a}}$$<br/>
$$a_2 = \frac{1}{b_2}$$<br/>
$$T_1 = T_0 + a_2$$<br/>

$$\textbf{Iterative Process} (\text{for i} \geq 2):$$<br/>
$$b_{2i} = \left(\frac{a_{2(i-1)}}{b_{2(i-1)}}\right)^{\frac{b}{a}}$$<br/>
$$a_{2i}= \frac{1}{b_{2i}}$$<br/>
$$T_i = T_{i-1} + a_{2i}$$<br/>

$$\text{Termination Conditions:}$$<br/>
$$\text{If } T > c \text{ and } \text{round}(T) = c: $$
$$\quad d = \text{first three decimal digits of } T $$
$$\quad \text{If } d \neq 0: T = \frac{T}{d} $$
$$\quad \text{Return } T $$
$$\text{If } i > \text{max iterations}: $$
$$\quad \text{Return } T $$
$$\text{Continue while } T \leq c$$
