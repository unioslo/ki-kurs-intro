"""
Canvas-compatible collapsible exercise/solution and question/answer directives.
Uses HTML5 details/summary for no-JavaScript collapsibility.
"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class canvas_exercise(nodes.General, nodes.Element):
    """Container for exercise."""
    pass


class canvas_solution(nodes.General, nodes.Element):
    """Container for solution (collapsible)."""
    pass


class canvas_question(nodes.General, nodes.Element):
    """Container for question."""
    pass


class canvas_answer(nodes.General, nodes.Element):
    """Container for answer (collapsible)."""
    pass


class CanvasExerciseDirective(SphinxDirective):
    """
    Canvas exercise directive.

    Usage::

        .. canvas-exercise::

           Exercise content here

           .. canvas-solution::

              Solution content here (will be collapsible)
    """
    has_content = True

    def run(self):
        node = canvas_exercise()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class CanvasSolutionDirective(SphinxDirective):
    """Collapsible solution directive."""
    has_content = True

    def run(self):
        node = canvas_solution()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def html_visit_canvas_exercise(self, node):
    """Generate exercise HTML - will contain nested solution."""
    # Check if this exercise has a nested solution
    has_solution = any(isinstance(child, canvas_solution) for child in node.children)

    self.body.append('<div class="canvas-exercise">\n')
    self.body.append('<div class="exercise-icon">🤔</div>\n')
    self.body.append('<div class="exercise-content">\n')

    # Store state for depart function
    node['has_solution'] = has_solution


def html_depart_canvas_exercise(self, node):
    """Close exercise HTML."""
    if not node.get('has_solution'):
        self.body.append('</div>\n')  # Close exercise-content
    self.body.append('</div>\n')  # Close canvas-exercise


def html_visit_canvas_solution(self, node):
    """Generate collapsible solution HTML using details/summary (nested in exercise)."""
    self.body.append('</div>\n')  # Close exercise-content
    self.body.append('<details class="canvas-solution">\n')
    self.body.append('<summary><strong>💡 Løsning / Solution</strong> (klikk for å vise)</summary>\n')
    self.body.append('<div class="solution-content">\n')


def html_depart_canvas_solution(self, node):
    """Close solution HTML."""
    self.body.append('</div>\n')  # Close solution-content
    self.body.append('</details>\n')  # Close details


class CanvasQuestionDirective(SphinxDirective):
    """
    Canvas question directive.

    Usage::

        .. canvas-question::

           Question content here

           .. canvas-answer::

              Answer content here (will be collapsible)
    """
    has_content = True

    def run(self):
        node = canvas_question()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class CanvasAnswerDirective(SphinxDirective):
    """Collapsible answer directive."""
    has_content = True

    def run(self):
        node = canvas_answer()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def html_visit_canvas_question(self, node):
    """Generate question HTML - will contain nested answer."""
    # Check if this question has a nested answer
    has_answer = any(isinstance(child, canvas_answer) for child in node.children)

    self.body.append('<div class="canvas-question">\n')
    self.body.append('<div class="question-icon">❓</div>\n')
    self.body.append('<div class="question-content">\n')

    # Store state for depart function
    node['has_answer'] = has_answer


def html_depart_canvas_question(self, node):
    """Close question HTML."""
    if not node.get('has_answer'):
        self.body.append('</div>\n')  # Close question-content
    self.body.append('</div>\n')  # Close canvas-question


def html_visit_canvas_answer(self, node):
    """Generate collapsible answer HTML using details/summary (nested in question)."""
    self.body.append('</div>\n')  # Close question-content
    self.body.append('<details class="canvas-answer">\n')
    self.body.append('<summary><strong>💡 Svar / Answer</strong> (klikk for å vise)</summary>\n')
    self.body.append('<div class="answer-content">\n')


def html_depart_canvas_answer(self, node):
    """Close answer HTML."""
    self.body.append('</div>\n')  # Close answer-content
    self.body.append('</details>\n')  # Close details


def setup(app):
    """Register the Canvas exercise and question directives."""
    app.add_node(
        canvas_exercise,
        html=(html_visit_canvas_exercise, html_depart_canvas_exercise)
    )
    app.add_node(
        canvas_solution,
        html=(html_visit_canvas_solution, html_depart_canvas_solution)
    )
    app.add_node(
        canvas_question,
        html=(html_visit_canvas_question, html_depart_canvas_question)
    )
    app.add_node(
        canvas_answer,
        html=(html_visit_canvas_answer, html_depart_canvas_answer)
    )

    app.add_directive('canvas-exercise', CanvasExerciseDirective)
    app.add_directive('canvas-solution', CanvasSolutionDirective)
    app.add_directive('canvas-question', CanvasQuestionDirective)
    app.add_directive('canvas-answer', CanvasAnswerDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
