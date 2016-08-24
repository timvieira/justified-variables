Justified Variables
===================

I like it when my source code lines up nicely, don't you? Let's put an end to
ugly pairings, such as `open/close`, `alpha/beta`, `vertex/edge`. Let's see more
of `open/shut`, `node/edge`, `push/pull`!

These typographic constraints can make coding feel like a crossword puzzle.

`justified variables` are clusters of related words of the same length
(`justified` in fixed-width font). We're particularly interested in word
clusters with contrasting meanings, part-whole, antonyms, and frequently
associated programming / math jargon (`variables`). Standard abbreviations are
gladly accepted.

2
===
```
- hi
  lo  ["high" and "low" points in an interval]
```

3
===
```
- foo  [When you just don't care]
  bar
  baz
 (goo)
 (boo)
 (bla)

- pro
  con

- yay  [Instead of yes/no?]
  nay

- add  [Numeric operations]
  sub
  mul
  div
  neg
  pow
  mod
  inv
  abs
  cmp
  exp
  log
  sin
  cos
  tan
 (int)

- and  [Boolean operations]
  xor
  not
  (but not or)

- top (⊤)  [Aliases for true and false; popular in logic programming]
  bot (⊥)

- get  [Common in method names / prefixes]
  set/put

- bar  [as in \bar{y} and \hat{y}]
  hat

- min
  max
 (mid)

- std
  avg

- was
  now

- old
  new

- err  [Common when testing numerical code]
  tol
  eps
  rel
  abs

- car  [lisp's list manipulations]
  cdr

- tic  [Goes the clock, timing code]
  toc

- day
  eve
```

4 ("knuckle tattoos")
=====================
```
- love
  hate

- n00b
  l33t

- loss
  gain
  risk
  cost

- tree  [Parsing terminology]
  item
  span
  rule
  word
  node
  edge

- user
  pass

- hope
  fear

- slow
  fast

- push
  pull

- this
  that

- node
  edge

- some  [the option type]
  none

- head
  body

- head
  tail
  last
  list

- cons
  snoc

- flip
  flop

- sink
  swim

- todo
  done

- prev
  next
  curr

- save
 (dump)
  load
 (read)
 (file)

- shut
  open
 (seek)
 (read)
 (file)

- dawn
  dusk

- redo
  undo

- stop
  play
  step
  stay
  seek

- hide
  seek
  hunt
  find

- geek
  jock
  dork

- more
  less

- pass
  fail

- done
  init
  halt

- door
  knob

- skim
  read

- warm
  cool/cold

- evil
  good

- foot
  hand

- kind
  mean
  nice

- firm
  soft

- rich
  poor

- fake
  real

- tick
  tock

- ping
  pong

- unit
  pair
  quad

- rise
  fall

- fair  [Baseball]
  foul

- verb
  noun
 (prep) [but not det, adj, adv]
```

5
===
```
- fixed  [Something we care a lot about here]
  width
  fonts

- later  [Scheduling tasks]
  never
  maybe  (instead of 'someday')
 (tasks)

- start  [Instead of ``start/stop`` or ``begin/end``]
  cease

- alpha  [Biblical beginning and end]
  omega

- noisy  [signal processing]
  clean

- major
  minor
 (equal)
 (sharp)
 (music)

-   child
  | adult
  = human

-   nodes
  + edges
  = graph

- numpy  [I <3 scientific programming in python]
  scipy
  pylab

-  right
 + wrong
 = total
  (tests)
  (cases)

- split
  merge

- shape
  scale

- guess
  truth

- inner
  outer

- upper
  lower

- small
  large

- above
  below

- sleek
  hairy

- drive
  crash

- spicy
  bland

- slide
  stick

- store
  flush

- flora
  fauna

- salty
  sweet

- pants
  shirt
  skirt
  jeans
  shoes
  socks

- these
  those

- robot
  human

- throw  [Exception handling, or dogs]
  catch
  fetch

- raise
  lower

- notes  [Headings of my todo list]
  ideas
  learn
  links
  todos
```

6
===
```
- reward
  punish

- encode
  decode
 (solver)
 (reader)

- arrive
  depart

- accept   [MCMC algorithms]
  reject
 (kernel)
 (random)
 (sample)

-  prefix
 + suffix
 = string

- source
  target

-   frozen  [Financial jargon]
  | liquid
  = assets

- linear [Functions properties]
  affine
  convex
 (smooth)
 (but not concave,
          monotone,
          constant,
          monotonic,
          quadratic,
          piecewise,
          polynomial,
          continuous,
          differentiable)

- scarce
  plenty

- target  [Testing jargon]
  expect
  actual
  result

- insane
  placid

- before
  within

- chunky
  gritty
  smooth

- ignore
  invite

- resume
  desist

- insert
  inject
  delete
  remove

- create  [File objects]
  unlink

- single
  double
  triple

- ignite
  defuse

- server  [Networking jargon]
  client
  subnet

- public  [Encryption keys]
  secret
  shared

- scalar  [Linear algebra types]
  vector
  matrix
  tensor
 (number)
 (double)

- crunch
  squish
  squash
  splash
  splosh

- repeat
  return
  finish
```

7
===
```
- explore
  exploit
 (dilemma) [reinforcement learning]

- softmax  [probability and neural networks]
  sigmoid
  rectify

- calorie
  protein

- reverse
  forward

- success
  failure

- enqueue
  dequeue

- respond
  decline

- mustard
  ketchup

- summary
  details

- provide
  require

- advance
  retreat
  regroup

- collect  [Plotting?]
  scatter
  diffuse
  dissect
  isolate

- abandon
  restore
  recover
 (session)

- greater
  reduced

- gradual
  stepped

- prevail
  succumb

- precede
  succeed

- morning
  evening

- Viterbi [semirings]
  Boolean
```

8
===
```
- question
  response

- document
  sentence

- positive
  negative
 (unsigned)

- username
  password

- analytic (e.g., analytic
  estimate        solution
                  compared
               to sampling
                  estimate)

- adjacent
  opposite (but not hypotenuse or SOHCAHTOA)

- maximize
  minimize
  optimize
 (criteria)
 (function)
 (but not objective)

- majority
  minority
  equality

- increase
  decrease

- function
  gradient
  Jacobian
  calculus (but not Hessian)

- observed
  expected (gradient of an exponential family)

- position
  velocity
 (dynamics)
 (simulate)

- proposal
  sampling

- alphabet
  features

- incoming
  outgoing

- expected
  actually
  achieved
 (unittest)

- combined
  separate

- chowdown
  showdown

- inferior
  superior (rather than worse/better)
```

9
===
```
- justified  [In case you didn't get it.]
  variables

- predicate
  arguments
 (relations)

- annotated  [Semi-supervised learning]
  unlabeled
 (bootstrap)

- injective
  bijective
  (but not surjective)

- originate
  terminate

- inclusive
  exclusive

- exploding  [Deep learning folklore]
  vanishing
 (gradients)
 (recurrent)
 (neuralnet)

- increased
  decreased
  unchanged

- preceding
  following
```

10
===
```
- surjective  [Properties of relations]
  one-to-one (= injective)
  invertible (= bijective)

- conclusion
  motivation
  experiment
  background
  references

- randomized
  repeatable
```

11
===
```
- exponential
  logarithmic

- specificity (=precision)
  sensitivity (=recall)
 (error_types)

- variational
  statistical
  expectation
  observation
```

12
===
```
- bibliography
  introduction
```

Greek letters
=============
```
- mu
  nu
  xi
  pi

- eta
  rho
  tau
  phi
  chi
  psi

- zeta
  beta
  iota

- omega
  sigma

- alpha
  gamma
  delta
  theta
  kappa

- lambda  (is to loneliest Greek letter)

- epsilon
  omicron
  upsilon
```
