Justified Variables
===================

I like it when my source code lines up nicely, don't you?

This document is here to
```
help
make
your
code
look
nice
```

Let's put an end to ugly pairings, such as `open/close`, `alpha/beta`,
`vertex/edge`. Let's see more of `open/shut`, `node/edge`, `push/pull`!

These typographic constraints can make coding feel like a crossword puzzle.

```
coding
x-word
puzzle
```

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

- yae/yay  [Instead of yes/no?]
  nay

- win  [Video games]
  die

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
  ior  [= inclusive or]

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

- dry
  wet
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

- gold  [= the_truth]
  pred  [= predicted]
 (auto) [= automatic]

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

- orig
  term

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

- move
  stay

- stop
  play
  step
  stay
  seek

- hide
  show
  seek
  hunt
  find

- geek
  jock
  dork

- more
  less

- loud
  soft

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

- idle
  busy
 (work)

- lady
  lord

- east
  west

- tick
  tock

- ping
  pong

- bear  [stock market]
  bull

- unit
  pair
  quad

- rise
  fall

- fair  [Baseball]
  foul

- home
  away
 (game)

- dead
  live

- tame
  wild

- give
  take

- fire
  hire

- verb
  noun
 (prep) [but not det, adj, adv]

- from  [Instead of begining/end start/finish]
  upto

- sans (without)
  avec (with)
```

5
===
```
- fixed  [Something we care a lot about here]
  width
  fonts

- fresh
  stale

- stack  [Transition-based parsing]
  queue
 (parse)

- later  [Scheduling tasks]
  never
  maybe  (instead of 'someday')
 (tasks)

- start  [Instead of ``start/stop`` or ``begin/end``]
  cease

- first  [Instead of ``start/stop`` or ``begin/end``]
  final

- alpha  [Biblical beginning and end]
  omega

- enter  [Instead of `enter/exit`]
  leave

- began  [Instead of start/end, if past tense is appropriate.]
  ended

- tasty
  nasty

- noisy  [signal processing]
  clean

- north
  south

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

- token  [natural language processing. don't use words/labels]
  label
  topic  [for unsupervised :-)]

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

- raise
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

- slope   [Lines]
  angle

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

- reward   [Reinforcement learning]
  action
  policy
 (oracle)  [Imitation learning]
 (expert)
 (but not state
          trace/history/trajectory
          episode)

- encode
  decode
 (solver)
 (reader)

- arrive
  depart

- better
  worsen

- gossip
  gospel

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

- inputs
  target    [e.g., learning a function: R^n -> n]

- lookup    [data structures methods]
  update
  insert

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

- spring
  summer
  autumn
  winter
 (season)

- former
  middle
  latter

- random
  sorted
 (stream)

```

7
===
```
- defunct
  current
  updated
  
- explore
  exploit
 (dilemma)  [reinforcement learning]

- teacher
  student

- explore  [bonus reinforcement learning]
  exploit
  rewards
  actions
  bandits
  learner
  weights  [(contextual) bandits, EXP3/EXP4]
  experts

- grammar
  lexicon

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
- business
  pleasure

- question
  response

- document
  sentence

- positive
  negative
 (unsigned)

- conjunct
  disjunct

- username
  password

- analytic (e.g., analytic
  estimate        solution
                  compared
               to sampling
                  estimate)

- explicit
  implicit

- beginner
  advanced

- adjacent
  opposite (but not hypotenuse or SOHCAHTOA)

- practice
  appraise
  consider
  evaluate

- maximize
  minimize
  optimize
 (criteria)
 (function)
 (suchthat) <- instead of "subjectto"
 (but not objective or constraint/condition)

- majority
  minority
  equality

- increase
  decrease

- function
  gradient
  Jacobian
  calculus (but not Hessian)
 (variable)

- observed
  expected (gradient of an exponential family)

- features  [machine learning terms]
  examples
 (learning)

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

- constant
  variable

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

- commence
  complete
```

9
===
```
- justified  [In case you didn't get it.]
  variables

- hindsight
  foresignt

- diagnosis
  treatment

- synthetic
  realistic

- completed
  remaining

- predicate
  arguments
 (relations)

- injective
  bijective
  (but not surjective)

- originate  [Instead of begin/end; start/end]
  terminate

- inclusive
  exclusive

- increased
  decreased
  unchanged

- preceding
  following

- annotated  [Semi-supervised learning]
  unlabeled
 (bootstrap)

- typically
  sometimes
  everytime
 (nowayjosé)
 (neverever)

- exploding  [Deep learning folklore]
  vanishing
 (gradients)
 (recurrent)
 (neuralnet)

- deductive
  inductive
 (databases)
 (inference)
 (knowledge)

```

10
===
```
- surjective  [Properties of relations]
  one-to-one (= injective)
  invertible (= bijective)

- excitation
  inhibition

- consequent  [dependency graphs]
  antecedent
 [dependency]
 [downstream]

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

- intensional [terms from deductive databases]
  extensional

- variational
  statistical
  expectation
  observation

- abstraction [the two operations of the λ calculus
  application

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

- lambda  (is the loneliest Greek letter)

- epsilon
  omicron
  upsilon
```
