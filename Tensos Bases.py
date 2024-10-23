import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf





#initializarea unui tensor

g = tf.constant(4, shape=(4,3), dtype=tf.float32)
x = tf.constant([[1, 2, 3], [4, 5, 6]], shape=(2,3))
x = tf.ones((4,4), dtype =tf.int32)

y = tf.zeros((4,5))
b = tf.eye((6))
v = tf.random.normal((3,2), mean=0, stddev=4)
h = tf.random.uniform((3,2), minval=3, maxval=6)
t = tf.range(start=10, limit=20, delta=2, dtype=tf.float32 )

print(g)
print(x)
print(y)
print(b)
print(v)
print(h)
print(t)

#matematica cu tensori

a = tf.constant([10,10,10])
e = tf.constant([2, 3, 4])
k = tf.add(a, e)
print(k)

o = tf.constant([10,7,9])
p = tf.constant([3,5,7])
l = tf.subtract(o, p)
print(l)

m = tf.constant([4, 5, 6])
n = tf.constant([2, 1, 2])
q = tf.divide(m, n)
print(q)

i = tf.constant([2, 7, 8])
u = tf.constant([3, 7, 6])
f = tf.multiply(i, u)
print(f)

#indexarea
j = tf.constant([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(j[:5:])


#remodelarea tensorilor

s = tf.range(18)
print(s)

s = tf.reshape(s,(9 ,2)
               )
print(s)