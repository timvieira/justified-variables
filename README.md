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
  
- eq  [ == ]
  ne  [ != ]
  le  [ <= ] 
  lt  [ <  ]
  gt  [ >  ]
  ge  [ >= ]
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

- yea/yae/yay  [Instead of yes/no?]
  nay

- win  [Video games]
  die

- mom
  dad

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

- all  [quantifiers]
  any

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

- src  [Abbr. `source/target`]
  trg

- tgt  [Abbrev. `target/destination`]
  dst

- bid  [Auction]
  ask
 (buy)

- row  [like in a table]
  col

- idx
  key
  ptr
  ref
  tab
  tag

```

4 ("knuckle tattoos")
=====================
```
- love
  hate

- have
  lack
 (miss)

- have  [Testing: Alternative for `got/want` and `actual/expected` #21]
  want

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
  leaf

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
  self

- node
  edge

- some  [the option type]
  none

- only
  many

- keep
  drop

- head
  body

- lady
  lord

- ride  [Getting from A to B]
  walk

- head/init
  tail/rear
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

- hard
  soft

- save
 (dump)
  load
 (read)
 (file)

- file  [ organization ]
  pile

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

- full
  thin

- stop
  play
  step
  stay
  seek

- hide
  show
- hide
  seek
  hunt
  find
  lose

- geek
  jock
  dork
  nerd

- more
  less

- loud
  soft

- pass
  fail

- done
  init
  halt

- tame
  wild

- door
  knob

- skim
  read

- warm/heat
  cool/cold

- evil
  good

- foot
  hand
  head
  body

- kind
  mean
  nice

- firm
  soft

- rich
  poor/lean

- fake
  real

- idle
  busy/work

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

- rise  [Alternative for growth/decay #20]
  fall

- fair  [Baseball]
  foul

- home
  away
 (game)

- dead
  live

- give
  take

- fire
  hire

- verb
  noun
 (prep) [but not det, adj, adv]

- from  [Instead of begining/end start/finish]
  upto

- maxi
  mini

- anal  [Thermometer placement]
  oral

- sans (without)
  avec (with)

- temp [also temporary]
  perm [     permanent]

- fork [processes or threads]
  kill
  reap
```

5
===
```
- fixed  [Something we care a lot about here]
  width
  fonts

- query
- reply

- bless
  curse

- fresh
  stale

- birth
  death

- stack
  queue

- empty
  inuse

- later  [Scheduling tasks]
  never
  maybe  (instead of 'someday')
  delay
 (tasks)

- start  [Instead of ``start/stop`` or ``begin/end``]
  cease
 (begin)
 (belay)

- first  [Instead of ``start/stop`` or ``begin/end`` #7]
  final

- alpha  [Biblical beginning and end]
  omega

- enter  [Instead of `enter/exit`]
  leave

- began  [Instead of start/end, if past tense is appropriate #7.]
  ended

- fancy
  plain

- piano  [Musical version of soft/hard]
  forte

- tasty
  nasty

- brave
  timid

- noisy/dirty  [Signal processing]
  clean

- noisy
  quiet

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

- shape  [ Parameters of many probability distributions ]
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

- black
  white

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
  umami

- heavy
  light

- pants
  shirt
  skirt
  jeans
  shoes
  socks
  scarf

- leaky/loose  [Abstractions, bounds, and faucets]
  tight

- these
  those

- relax
  tense

- robot
  human

- throw  [Exception handling, ball sports, dogs]
  catch
  fetch
 (raise)

- raise
  lower
 (level)

- rural
  urban

- stand
  yield

- notes  [Headings of my todo list]
  ideas
  learn
  links
  todos

- build
  decay

- payed  [Purchasing, slightly "payed" is a work around for "paid"]
- given

- start  [Asynchronous operations]
  begin
  abort
  close
  await
  block
  sleep
  delay
  pause

- photo  [Types of audiovisual media]
  video
  audio
  image

- free  [Memory/resource allocation]
  used

- free  [Pricing]
  paid
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

- export
  import

- mother
  father
  parent

- forbid
  permit

- arrive
  depart

- better
  worsen

- gossip
  gospel

- accept   [MCMC algorithms]
  reject/refuse
 (kernel)
 (random)
 (sample)

- affirm
  negate

- gather
  spread  [instead of scatter]

-  prefix
 + suffix
 = string
  (middle)

- source
  target

- abduct   [Biomechanics alternative for away/towards, but I can never remember which is which...]
  adduct

- inputs
  target    [e.g., learning a function: R^n -> n]

- lookup    [data structures methods]
  update
  insert
  inject
  delete
  remove
  search
  exists
  filter
  length

- active  [Component status]
  unused
  failed

- waxing
  waning

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

- attach
  detach

- attack
  defend

- benign
  malign

- target  [Testing jargon]
  expect
  actual
  result

- insane
  placid

- better
  worsen

- danger
  safety

- junior
  senior

- partly
  wholly

- supply
  demand

- divest
  invest

- single
  double
  triple

- before
  within

- chunky
  gritty
  smooth

- ignore
  notice/invite

- resume
  desist

- harden
  soften

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
  signed

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

- expand
  reduce

- mother
  father
  sister
 [family]
 [member]
 (but not brother)

- signal [Multi-threaded programming]
  notify

- reader [Multi-threaded programming]
  writer

- master [Multi-threaded programming]
  worker

- forall  [ Predicate logic ]
  exists
```

7
===
```
- antonym
  synonym

- clarity
  opacity

- defunct
  current
  updated

- explore
  exploit
 (dilemma)  [reinforcement learning]

- teacher
  student

- closing   [Finally open/close can be together]
  opening

- conform
  deviate

- correct
  falsify

- consume
  abstain

- advance  [Another alternative for forward/backward]
  retreat

- fertile
  sterile

- explore  [bonus reinforcement learning]
  exploit
  rewards
  actions
  bandits
  learner
  weights  [(contextual) bandits, EXP3/EXP4]
  experts

- offense
  defense

- pinning  [Term I've used to instead of to force/eliminate a decision]
  pruning

- grammar
  lexicon

- general  [Cases]
  special

- softmax  [Neural networks]
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

- package
  version

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

- exclude
  include

- incline
  decline

- receive
  deliver

- explode
  implode

- failing
  passing

- present
  missing

- maximal/maximum
  minimal/minimum

- started  [Asynchronous operations]
  stopped

- pending  [Asynchronous operations]
  running
  waiting
  asleeep
  blocked
  aborted
  timeout

- created   [databases]
  updated
  deleted
 [fetched]  [for read]
 [visited]

- Viterbi [semirings]
  Boolean

- acquire  [Multi-threaded programming]
  release

- readers [Multi-threaded programming]
  writers

- numeric
  textual

- heading
  content
```

8
===
```
- producer
  consumer

- question
  response

- business
  pleasure

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

- implicit
  explicit

- interior
  exterior

- internal
  external

- beginner
  advanced

- adjacent
  opposite (but not hypotenuse or SOHCAHTOA)

- practice
  appraise
  consider
  evaluate

- hardware
  software

- inclined
  vertical
 [climbing]

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

- monosemy
  polysemy

- increase
  decrease

- singular
  multiple

- porosity
  solidity

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

- absolute
  relative
 [position]

- strength
  weakness

- chowdown
  showdown

- inferior
  superior (rather than worse/better)

- abstract
  concrete

- commence  [Alternatives for start/end #7]
  complete
  conclude
  continue
  postpone

- backhand
  forehand

- civilian
  military

- confined
  invasive

- dissuade
  persuade
 [argument]

- employee
  employer
 [jobplace]

- datetime
  duration

- writable
  readable
```

9
===
```
- justified  [In case you didn't get it.]
  variables

- hindsight
  foresignt

- expansion  [Alternative to growth/decay #20]
  reduction

- diagnosis
  treatment

- synthetic
  realistic

- completed
  remaining

- activator
  inhibitor

- conductor
  insulator

- confident
  diffident

- predicate
  arguments
 (relations)

- injective
  bijective
  (but not surjective)

- originate  [Instead of begin/end; start/end]
  establish
  terminate
  interrupt

- inclusive
  exclusive

- increment
  decrement

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

- plaintiff
  defendant

- inflation
  deflation

- preserved
  destroyed

- energetic
  lethargic

- deductive
  inductive
  abductive
 (databases)
 (inference)
 (knowledge)

- different [Value comparison, types of twins]
  identical
  fraternal

- lowercase
  uppercase

- destroyed
  preserved

- energetic
  lethargic

- temporary
  permanent
  cacheable

- iterative
  recursive

- grayscale
  fullcolor
```

10
===
```
- surjective  [Properties of relations]
  one-to-one (= injective)
  invertible (= bijective)

- excitation
  inhibition

- accelerate
  decelerate

- antecedent
  subsequent

- appreciate
  depreciate

- consequent  [Dependency graphs]
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

- simplicity
  complexity

- detractors
 (protesters)
  supporters

- exhalation/expiration  [Breathing]
  inhalation/aspiration

- foreground
  background
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

- abstraction [the two operations of the λ calculus]
  application

- centralized [Networking]
  distributed
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
