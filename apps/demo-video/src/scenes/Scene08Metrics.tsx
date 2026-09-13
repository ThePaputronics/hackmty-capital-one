import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';
import { MetricCounter } from '../components/MetricCounter';
import benchmarkData from '../data/benchmark.json';

export const Scene08Metrics: React.FC = () => {
  const frame = useCurrentFrame();

  const totalEvals = Math.floor(interpolate(frame, [0, 40], [0, benchmarkData.results.summary.total_transfers_evaluated], { extrapolateRight: 'clamp' }));
  const appIntercepted = Math.floor(interpolate(frame, [15, 55], [0, benchmarkData.results.app_fraud_protection.intercepted], { extrapolateRight: 'clamp' }));
  const valIntercepted = Math.floor(interpolate(frame, [30, 70], [0, benchmarkData.results.app_fraud_protection.value_intercepted_mxn], { extrapolateRight: 'clamp' }));

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        padding: '0 120px',
      }}
    >
      <div style={{ marginBottom: '40px' }}>
        <span style={{ color: theme.colors.accent, fontFamily: theme.fonts.mono, fontSize: '15px', letterSpacing: '2px', textTransform: 'uppercase' }}>
          Validación Rigurosa · Benchmark Harness
        </span>
        <h2 style={{ color: '#fff', fontFamily: theme.fonts.serif, fontSize: '48px', margin: '6px 0 0 0' }}>
          Resultados Reproducibles del Motor
        </h2>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '24px', marginBottom: '40px' }}>
        <MetricCounter
          label="Transferencias"
          value={totalEvals}
          sublabel="180 personas · 426 PyMEs"
        />
        <MetricCounter
          label="APP Interceptados"
          value={`${appIntercepted} / ${benchmarkData.results.app_fraud_protection.attempts}`}
          sublabel="100% de recall en manipulación"
          highlight={true}
        />
        <MetricCounter
          label="Monto Protegido"
          value={`$${valIntercepted.toLocaleString('es-MX')}`}
          sublabel="Exposición simulada evitada"
          highlight={true}
        />
        <MetricCounter
          label="Falsos Positivos"
          value="0.0%"
          sublabel="0 alertas erróneas en comercios"
        />
      </div>

      {/* Latency footnote */}
      <div
        style={{
          backgroundColor: theme.colors.surface,
          border: `1px solid ${theme.colors.surfaceBorder}`,
          borderRadius: '10px',
          padding: '16px 24px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <span style={{ color: theme.colors.textSecondary, fontSize: '16px' }}>
          Latencia de inferencia en tiempo real:
        </span>
        <span style={{ color: theme.colors.accentLight, fontFamily: theme.fonts.mono, fontWeight: 700, fontSize: '18px' }}>
          p50: {benchmarkData.results.summary.latency_p50_ms} ms · p95: {benchmarkData.results.summary.latency_p95_ms} ms
        </span>
      </div>
    </div>
  );
};
