/**
 * Advent of Code 2022 Day 1 solution.
 */

import java.io.File

val testinp = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
  """.trimIndent()

/**
 * Get diff of List "as series", first element will be null.
 */
private fun diff(ints: List<Int>): List<Int?> {
  val diffs = ints.mapIndexed { idx, elem -> if (idx == 0) null else elem - ints[idx - 1] }
  return diffs
}

private fun getIncsCount(inp: String): Int {
  //val ints = listOf(1, 2, 3, 2, 1)
  val ints = inp.split("\n").map { it.toInt() };
  val diffs = diff(ints)
  val incs = diffs.filterNotNull().filter { it > 0 }.size
  //println(ints)
  //println(diffs)
  return incs
}

private fun getIncs3Count(inp: String): Int {
  //val ints = listOf(1, 2, 3, 2, 1)
  var ints = inp.split("\n").map{ it.toInt() };
  //println(ints.windowed(3))
  //println(ints.windowed(3).map{it.sum()})
  ints = ints.windowed(3).map{it.sum()}
  val diffs = diff(ints)
  val incs = diffs.filterNotNull().filter{ it > 0 }.size
  //println(ints)
  //println(diffs)
  return incs
}

private fun solve_day01_a(inp: String): Int {
  var lol = inp.split("\n\n").map{ it.split("\n").map{ it.toInt() } }
  var lolsums = lol.map{ it.sum() }
  //println(lolsums)
  return lolsums.max()
}

private fun solve_day01_b(inp: String): Int {
  var lol = inp.split("\n\n").map{ it.split("\n").map{ it.toInt() } }
  var lolsums = lol.map{ it.sum() }
  //println(lolsums::class.java.typeName)
  //println(lolsums[0]::class.java.typeName)
  var top3 = lolsums.sortedDescending().slice(0..2)
  return top3.sum()
}

//fun main(args: Array<String>){
fun main(){
  var res = solve_day01_a(testinp)
  println("day 01 pt 1 test-out=$res")

  val inp = File("./in/day01.in").readText().trim()
  res = solve_day01_a(inp)
  println("day 01 pt 1 result=$res")

  res = solve_day01_b(testinp)
  println("day 01 pt 2 test-out=$res")

  res = solve_day01_b(inp)
  println("day 01 pt 2 test-out=$res")
}
